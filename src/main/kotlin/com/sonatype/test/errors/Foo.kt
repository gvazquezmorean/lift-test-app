package com.sonatype.test.errors

class Foo {

    override fun toString(): String {
        throw IllegalStateException() // exception should not be thrown here
    }
}
