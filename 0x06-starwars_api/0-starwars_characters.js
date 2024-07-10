#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args.length === 0) {
    console.error("Usage: ./print_characters.js <Film ID>");
    process.exit(1);
}

const filmId = parseInt(args[0], 10);

function fetchCharacters(filmId) {
    const url = `https://swapi.dev/api/films/${filmId}/`;
    request(url, { json: true }, (error, response, body) => {
        if (error || !body.characters) {
            console.error("Error fetching characters:", error);
            return;
        }

        body.characters.forEach(characterUrl => {
            request(characterUrl, { json: true }, (err, res, charBody) => {
                if (err || !charBody.name) {
                    console.error("Error fetching character details:", err);
                    return;
                }
                console.log(charBody.name);
            });
        });
    });
}

fetchCharacters(filmId);
