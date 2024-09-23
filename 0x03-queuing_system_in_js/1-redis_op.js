const redis = require('redis');
const { promisify } = require('util');


const client = redis.createClient();
client.on('error', (error) => {
  console.log(`Redis not connected to server ${error}`);
});
client.on('connect', () => {
  console.log('Redis client is connected to server');
});
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, result) => {
    if(err) {
      console.log('Value for the key doesnot exist');
    }
    console.log(`${result}`)
  });
};
const mainfunction = () => {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}
mainfunction();

