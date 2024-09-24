const redis = require('redis');

const client = redis.createClient();

client.on('error', () => {
  console.log('Redis client not connected to server');
});

client.on('connect', () => {
  console.log('Redis client connected to server');
});

const keyValueObjects = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

for(const [key,value] of Object.entries(keyValueObjects)) {
  client.hset('HolbertonSchool', key, value, (err, result) => {
    if (err) {
      console.log(`Error setting hash: ${err}`);
    }
    console.log(`Reply: ${result}`);
  });
};

client.hgetall('HolbertonSchool', (err, result) => {
  if (err) {
    console.log(`Error retreving hash: ${err}`)
  }
  console.log(result);
});
