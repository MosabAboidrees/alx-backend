#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

// Create a Redis client instance
const redisClient = createClient();

// Event listener for errors
redisClient.on('error', (error) => {
  console.error('Redis client not connected to the server:', error.message);
});

/**
 * Updates a hash field in Redis with the provided value.
 * @param {string} hashKey - The name of the Redis hash.
 * @param {string} fieldKey - The field name within the hash.
 * @param {number} fieldValue - The value to assign to the field.
 */
const updateHashField = (hashKey, fieldKey, fieldValue) => {
  redisClient.HSET(hashKey, fieldKey, fieldValue, print); // Use HSET to update the hash
};

/**
 * Fetches and logs all fields and values of a hash from Redis.
 * @param {string} hashKey - The name of the Redis hash to retrieve.
 */
const logHashContents = (hashKey) => {
  redisClient.HGETALL(hashKey, (error, reply) => {
    if (error) {
      console.error(`Error retrieving hash ${hashKey}:`, error.message);
    } else {
      console.log(reply); // Log the hash contents
    }
  });
};

/**
 * Main function to update a Redis hash and display its contents.
 */
function main() {
  // Object representing school locations and their student counts
  const schoolLocations = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  // Update the hash with school location data
  for (const [location, studentCount] of Object.entries(schoolLocations)) {
    updateHashField('HolbertonSchools', location, studentCount);
  }

  // Log the contents of the updated hash
  logHashContents('HolbertonSchools');
}

// Event listener for successful connection to Redis server
redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
  main(); // Execute the main function once connected
});
