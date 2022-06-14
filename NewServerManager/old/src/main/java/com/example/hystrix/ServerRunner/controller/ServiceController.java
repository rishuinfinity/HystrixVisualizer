package src.main.java.com.example.hystrix.ServerRunner.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.example.hystrix.ServerRunner.delegate2.ServiceDelegate2;

@RestController
public class ServiceController {
	@Autowired
	ServiceDelegate2 serviceDelegate2;

	@RequestMapping(value = "/get-running-status/{input}", method = RequestMethod.GET)
	public String getStudents(@PathVariable String input) {
		System.out.println("Going to call services to to get data corresponding to input!");
		return serviceDelegate2.callServiceAndGetData(input);
	}
}
