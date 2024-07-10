#!/usr/bin/node

const request = require('request-promise');
const args = process.argv.slice(2);

if (args.length === 0) {
  console.error('Usage: ./print_characters.js <Film ID>');
  process.exit(1);
}

const filmId = parseInt(args[0], 10);

async function fetchCharacters (filmId) {
  try {
    const url = `https://swapi.dev/api/films/${filmId}/`;
    const filmResponse = await request({ uri: url, json: true });

    const promises = filmResponse.characters.map(async (characterUrl) => {
      const characterResponse = await request({ uri: characterUrl, json: true });
      return characterResponse.name;
    });

    const characterNames = await Promise.all(promises);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error('Error fetching characters:', error);
  }
}

fetchCharacters(filmId);
