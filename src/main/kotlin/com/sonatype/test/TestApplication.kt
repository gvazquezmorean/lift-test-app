package com.sonatype.test

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class TestApplication

fun main(args: Array<String>) {
    val str = "hello world"
	runApplication<TestApplication>(*args)
}
