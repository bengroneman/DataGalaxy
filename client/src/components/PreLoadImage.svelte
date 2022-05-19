<script>
	import env from '../lib/env.js';

	const BASE_URL = env.baseUrl;
	export let image = {
		name: 'Random image',
		src: 'https://picsum.photos/200/300/?random',
		alt: 'Random image',
		id: ''
	};

	const preload = async (id) => {
		const res = await fetch(`${BASE_URL}api/images/` + id, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		});

		let _blob = await res.blob();

		return new Promise(function (resolve) {
			let reader = new FileReader();
			reader.readAsDataURL(_blob);
			reader.onload = () => resolve(reader.result);
		});
	};
</script>

{#await preload(image.id) then base64}
	<figure class="aspect-square w-full">
		<img
			src={base64}
			alt={image.name}
			id={image.name + image.id}
			class="object-cover shadow-lg rounded-lg mx-auto"
		/>
		<figcaption>{image.category}</figcaption>
	</figure>
{/await}
