import adapter from '@sveltejs/adapter-netlify';
import dotenv from 'dotenv';
import preprocess from 'svelte-preprocess';

dotenv.config();

/** @type {import('@sveltejs/kit').Config} */
const config = {
	compilerOptions: {
		hydratable: true
	},
	preprocess: preprocess({
		replace: [["process.env.VITE_MODE", process.env.VITE_MODE]],
	}),
	kit: {
		adapter: adapter(),
		trailingSlash: 'always',
		prerender: {
			default: true
		}
	},
};

export default config;
