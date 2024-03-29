/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*"],
  theme: {
    extend: {
      // colors: {
      //   primary:"#fffbf7",
      //   secondaryp:"#fed1fa",
      //   secondaryo:"#fb6242",
      //   secondaryg: "#ceec87",
      //   button: "#e87b38",
      //   buttonhover: "#f8c23a",
      // },
      colors: {
        primary:"#0b0b2b",
        secondaryp:"#fed1fa",
        secondaryo:"#fb6242",
        secondaryg: "#ceec87",
        button: "#e87b38",
        buttonhover: "#f8c23a",
        textcol : "#ffffff"
      },
      fontFamily: {
        
        webFont: ['Raleway', 'sans-serif'],

      },
    },
    plugins: [],
  },
};