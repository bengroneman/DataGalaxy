<script>
	const preload = async (id) => {
		const res = await fetch('http://localhost:8000/api/images/' + id, {
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

	export let image = {
		src: 'https://picsum.photos/200/300/?random',
		alt: 'Random image',
		id: ''
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
	</figure>
{/await}
