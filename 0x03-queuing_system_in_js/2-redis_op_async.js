#!/usr/bin/yarn dev

import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();

// Listen for the 'connect' event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Promisify the client.get function
const getAsync = promisify(client.GET).bind(client);

/**
 * Sets a key-value pair in Redis
 * @param {string} schoolName - The key
 * @param {string} value - The value to set
 */
function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

/**
 * Retrieves and logs the value of a key from Redis using async/await
 * @param {string} schoolName - The key to retrieve
 */
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving key ${schoolName}: ${err.message}`);
  }
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
