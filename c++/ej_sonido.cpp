#include <SFML/Audio.hpp>

int main() {
    // Cargar un archivo de sonido
    sf::SoundBuffer buffer;
    if (!buffer.loadFromFile("ruta/del/archivo.wav")) {
        return -1; // Error al cargar el archivo
    }

    // Crear un objeto de sonido y establecer su buffer
    sf::Sound sound;
    sound.setBuffer(buffer);

    // Reproducir el sonido
    sound.play();

    // Mantener la aplicación abierta hasta que se haya completado la reproducción
    while (sound.getStatus() == sf::Sound::Playing) {
        // Esperar
    }