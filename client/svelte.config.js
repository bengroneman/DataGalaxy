//import adapter from '@sveltejs/adapter-netlify';
import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	compilerOptions: {
		hydratable: true
	},
	kit: {
		adapter: adapter(),
		trailingSlash: 'always',
		prerender: {
			default: true
		}
	}
};

export default config;
