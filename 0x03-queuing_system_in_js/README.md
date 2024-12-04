# 0x03-queuing_system_in_js


# Redis Queuing System

## Description
This project demonstrates the setup and basic usage of a Redis instance to perform simple operations, such as setting and retrieving key-value pairs.

## Steps to Set Up
1. Downloaded Redis version 6.0.10.
2. Extracted and compiled Redis.
3. Started the Redis server.
4. Verified server functionality using `PING`.
5. Set and retrieved the key-value pair `Holberton: School`.
6. Stopped the server using its PID.
7. Copied the `dump.rdb` file to the project directory.

## Usage
1. Start the Redis server: `src/redis-server &`
2. Use the Redis CLI for operations: `src/redis-cli`.
3. To stop the server, find the PID and run `kill [PID]`.
