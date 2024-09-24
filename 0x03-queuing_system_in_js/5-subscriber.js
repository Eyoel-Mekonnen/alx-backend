const redis = require('redis');

const client = redis.createClient();
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
client.on('connect', () => {
  console.log('Redis client is connected to the server');
});
client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
  if (message === "KILL_SERVER") {
    client.unsubscribe();
    client.quit();
    return
  }
  console.log(`${message}`);
});
