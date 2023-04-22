/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{vue,html,js}", "index.html"],
  darkMode: "class",
  theme: {
    extend: {
      maxHeight: {
        '0': '0',
        xl: '36rem',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}