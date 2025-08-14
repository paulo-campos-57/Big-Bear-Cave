/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        pressStart: ['"Press Start 2P"', 'cursive'],
      },
      colors: {
        darkSlate: '#1B1F23',       // Noturno
        charcoal: '#2E3238',        // Pedra
        deepRed: '#B22222',         // Vermelho sangue
        golden: '#D4AF37',          // Ouro
        forestGreen: '#2E8B57',     // Floresta
        magicBlue: '#3B82F6',       // Azul místico
        purpleShadow: '#6A0DAD',    // Roxo arcano
        offWhite: '#F5F5DC',        // Pergaminho
        lightGray: '#D3D3D3',       // Cinza claro
      }
    },
  },
  plugins: [],
}
