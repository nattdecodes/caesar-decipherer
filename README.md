# 🥗 Caesar Decipherer
**No need to know the key!**

A Caesar cipher decipherer where the key and the deciphered message are automatically calculated (see below for how it works)

## How It Works
This command-line Python decipherer uses natural language processing to automatically decipher encrypted messages without requiring a key input.

By analyzing the ciphertext and leveraging linguistic and letter patterns (AKA frequently used words and average letter distributions), the program determines the most probable decryption key and produces the corresponding plaintext.

## ToDo
- [ ] Add support for spaceless encrypted messages
- [ ] Add support for more languages (suggestions are welcome!)
- [X] ~~Optimise using letter distribution~~

## Limitations
The program currently only supports uppercase and lowercase letters of the English alphabet. Other characters will be left unchanged.

## Contributing
Contributions to this project are welcome. Please open an issue or submit a pull request for any improvements or bug fixes.

## Thanks
Thank you to first20hours for the [English word list](https://github.com/first20hours/google-10000-english).
Thank you to evilpacket for the [English letter distribution file](https://gist.github.com/evilpacket/5973230)

## License
This is licensed under the [MIT License](https://mit-license.org/).
