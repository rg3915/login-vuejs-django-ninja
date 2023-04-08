# Instalando TailwindCSS

[Documentação](https://tailwindcss.com/docs/installation)

```
yarn add tailwindcss
```

### Instale o [TailwindCSS](https://tailwindcss.com/)

```
npm init
npm i -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/**/*.html",
    "./src/**/*.{js,ts,vue}"
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```
touch src/tailwind.css
```

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Instalando plugins e fontes

```
npm install -D @tailwindcss/typography
```

[Poppings](https://blog.logrocket.com/how-to-use-custom-fonts-tailwind-css)

```js
/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./public/**/*.html",
    "./src/**/*.{js,ts,vue}"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
        poppins: ['Poppins', 'sans-serif']
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
```

### Instalando forms

```
npm i -D @tailwindcss/forms
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    // ...
  },
  plugins: [
    require('@tailwindcss/forms'),
    // ...
  ],
}
```

### Instalando aspect-ratio

```
npm i -D @tailwindcss/aspect-ratio
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    // ...
  },
  corePlugins: {
    aspectRatio: false,
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
    // ...
  ],
}
```

### Instalando Tailwind CSS Multi Theme

https://github.com/estevanmaito/tailwindcss-multi-theme#tailwind-css-multi-theme

```
npm install tailwindcss-multi-theme
```

### Instalando esbuild

```
npm i esbuild
```

Edite `package.json`

```json
"scripts": {
  "build-css": "npx tailwindcss -i src/tailwind.css -o public/dist/tailwind.css --watch",
  "build-js": "npx esbuild src/alpine.js --outfile=public/dist/alpine.js --bundle --watch",
  "build": "npx tailwindcss -i src/tailwind.css -o public/dist/tailwind.css; npx prettier --write public/",
  "lint": "npx prettier --write public/"
}
```

### [Prettier](https://prettier.io/) (Opcional)

```
npm install --save-dev --save-exact prettier
```

```
echo {}> .prettierrc.json
```

```
cat << EOF > .prettierignore
# Ignore artifacts:
build
coverage
EOF
```

#### Rodando o Prettier

```
npx prettier --write public/
ou
npm run lint
```
