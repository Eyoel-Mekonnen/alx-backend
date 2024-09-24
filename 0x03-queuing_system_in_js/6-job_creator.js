const kue = require('kue');

const queue = kue.createQueue();

const obj = {
  phoneNumber: '0944067638',
  message: 'Uploading',
};

const job = queue.create('push_notification_code', 
  obj).priority('normal').save((err) => {
    if (err) {
      console.log('Notification job failed');
    }
    console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', (result) => {
  console.log('Notification job completed');
})
job.on('failed', (error) => {
  console.log('Notification job failed');
})
