package com.example.hystrix.ServerRunner;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.netflix.hystrix.dashboard.EnableHystrixDashboard;

@SpringBootApplication
@EnableHystrixDashboard
@EnableCircuitBreaker
public class ServerRunnerApplication {

	public static void main(String[] args) {
		SpringApplication.run(ServerRunnerApplication.class, args);
	}

}
