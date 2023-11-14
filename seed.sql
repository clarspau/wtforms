-- To start with creating a db

DROP DATABASE IF EXISTS  adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Charcoal', 'dog', 'https://i.pinimg.com/originals/96/8a/8b/968a8b830a0a8346e4dc5fe21934a15d.jpg', 3, 'Hyper and playful', 't'),
  ('Smores', 'cat', 'https://www.thesprucepets.com/thmb/CbNFQ13WLsI-MuP93lF8gTfj3cw=/1080x0/filters:no_upscale():strip_icc()/37868147_243349996310794_540614542934147072_n-5b69b2b046e0fb0050630e3d.jpg', 8, 'Shy but calm', 't'),
  ('Sheenkies', 'chicken', 'https://petkeen.com/wp-content/uploads/2021/11/chicken-and-its-eggs_PhotoSongserm_Shutterstock.jpg', null, null, 't'),
  ('Sir Enchi', 'hamster', null, null, null, 't');

