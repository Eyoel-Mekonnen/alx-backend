const redis = require('redis');

const client = redis.createClient();

const { promisify } = require('util');

client.on('error', (error) => {
  console.log('Redis client is not connected to server'); 
});
client.on('connect', () => {
  console.log('Redis client connected to server');
});
const setNewSchool = async (schoolName, value) => {
  //client.set(schoolName, value, redis.print)
  const setasync = promisify(client.set).bind(client);
  const result = await setasync(schoolName, value);
  console.log(`Reply: ${result}`);
};
const displaySchoolValue =  async (schoolName) => {
  const getasync = promisify(client.get).bind(client);
  const value = await getasync(schoolName);
  //console.log(`I am executed first: ${value}`);
  console.log(value);
};
const mainFunction = async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};
mainFunction();
/*
 For understanding how this will be done using promises

 const redis = require('redis');

 const client = redis.createClient();

 const { promisify } = require('util');

 client.on('error', (error) => {
   console.log('Redis client is not connected to server');
   })

 const setNewSchool = (newSchool, value) => {
   const setasync = promisify(client.set).bind(client);
   return setasync(newSchool, value);
 }
 const displaySchoolValue = (schoolName) => {
   const getasync = promisify(client.get).bind(client);
   return getasync(schoolName);
 }
 const mainFunction = () => {
   displaySchoolValue('Holberton')
     .then((value) => {
       console.log(value);
       return setNewSchool('HolbertonSanFrancisco', '100');
     })
     .then((value) => {
       console.log(value);
       return displaySchoolvalue('HolbertonSanFrancisco');
     })
     .then((value) => { const redis = require('redis');
       console.log(value);
     })
     .catch((erro) => {
       console.log(`Error occured ${error}`);
     });
 }
 */
