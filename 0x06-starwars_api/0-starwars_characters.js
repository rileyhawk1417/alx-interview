#!/usr/bin/node
const req = require('request');
const URL = 'https://swapi-api.hbtn.io/api';
const input = process.argv;

if (input.length > 2) {
  req(`${URL}/films/${input[2]}/`, (err, _, body) => {
    if (err) {
      console.error(err);
    }
    const castLink = JSON.parse(body).characters;
    const castName = castLink.map(
      (link) =>
        new Promise((resolve, reject) => {
          req(link, (e, __, castReqBody) => {
            if (e) {
              reject(e);
            }
            resolve(JSON.parse(castReqBody).name);
          });
        })
    );
    Promise.all(castName)
      .then((castNames) => console.log(castNames.join('\n')))
      .catch((errs) => console.error(errs));
  });
}
