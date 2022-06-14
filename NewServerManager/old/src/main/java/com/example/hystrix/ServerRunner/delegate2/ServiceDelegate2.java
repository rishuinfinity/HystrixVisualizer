package src.main.java.com.example.hystrix.ServerRunner.delegate2;

import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;

public class ServiceDelegate2 {
	@Autowired
	RestTemplate restTemplate;
	
	@HystrixCommand(fallbackMethod = "callServiceAndGetData_Fallback")
	public String callServiceAndGetData(String input) {
		System.out.println("Getting data for " + input);
		String response = restTemplate
				.exchange("http://localhost:8080/give-data-to-server-manager/{input}"
				, HttpMethod.GET
				, null
				, new ParameterizedTypeReference<String>() {
			}, input).getBody();

		System.out.println("Response Received as " + response + " -  " + new Date());

		return "NORMAL FLOW !!! - input -  " + input + " :::  output Details " + response + " -  " + new Date();
	}
	
	@SuppressWarnings("unused")
	private String callServiceAndGetData_Fallback(String schoolname) {
		System.out.println("Service is down!!! fallback route enabled...");
		return "CIRCUIT BREAKER ENABLED!!!No Response From Service at this moment. Service will be back shortly - " + new Date();
	}

	@Bean
	public RestTemplate restTemplate() {
		return new RestTemplate();
	}
}
