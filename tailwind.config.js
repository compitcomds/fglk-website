/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*"],
  theme: {
    aspectRatio: {
      none: 0,
      square: [1, 1],
      "16/9": [16, 9],
      "4/3": [4, 3],
      "21/9": [21, 9], // Add comma here
    },
    screens: {
      'sm': '340px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
    },
    extend: {
      colors: {
        primary: "#fffbf7",
        secondaryp: "#fed1fa",
        secondaryo: "#fb6242",
        secondaryg: "#3fc446",
        button: "#e87b38",
        buttonhover: "#f8c23a",
        textcol: "#000000",
        white_back: "#ffffff", // Corrected color value
      },
      fontFamily: {
        webFont: ['Raleway', 'sans-serif'],
      },
    },
  }, // Add closing bracket here
  variants: {
    aspectRatio: ['responsive'],
  }, // Add closing bracket here
  plugins: [
    require("tailwindcss-responsive-embed"),
    require("tailwindcss-aspect-ratio"),
  ],
};
