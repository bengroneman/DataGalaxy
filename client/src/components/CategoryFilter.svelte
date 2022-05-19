<script>
	// Utils
	// components
	import CheckIcon from '../components/icons/CheckIcon.svelte';
	import SelectorIcon from '../components/icons/SelectorIcon.svelte';
	// global variables
	export let options = [];
	export let label;
	export let selectedOption = 'General';
	let searching = false;
	// Search
	$: filteredInOptions = selectedOption
		? options.filter((option) => {
				if (typeof option === typeof '') {
					return option.toLowerCase().startsWith(`${selectedOption.toLowerCase()}`);
				}
		  })
		: options;
	// TODO: Build out a secondary row for not found items in light gray
	$: filteredOutOptions = selectedOption
		? options.filter((option) => {
				return !option.toLowerCase().startsWith(`${selectedOption.toLowerCase()}`);
		  })
		: [];
	// helper functions
	const startSearching = () => (searching = true);
	const stopSearching = (event) => {
		if (!event.srcElement.id.startsWith('combobox')) {
			searching = false;
		}
	};
	function handleBodyClick(event) {
		if (!event.srcElement.id.startsWith('combobox')) {
			searching = false;
		}
	}
	function selectOption(event) {
		selectedOption = event.target.innerText;
		setTimeout(() => {
			searching = false;
		}, 500);
	}
</script>

<svelte:body on:click|stopPropagation={handleBodyClick} />

<div class="relative mt-6">
	<label
		for="combobox"
		class="absolute -top-2 left-2 -mt-px inline-block px-1 bg-white text-xs font-medium text-gray-900"
		>{label}</label
	>
	<span class="absolute inset-y-0 left-0 flex items-center pl-1.5 pr-12 text-sky-500">
		<CheckIcon />
	</span>
	<input
		id="combobox"
		bind:value={selectedOption}
		on:keydown={startSearching}
		on:keyup={stopSearching}
		on:click|stopPropagation={startSearching}
		type="text"
		class="w-full rounded-md border border-gray-300 bg-white pl-12 py-2 pr-12 shadow-sm focus:border-orange-500 focus:outline-none focus:ring-1 focus:ring-orange-500 sm:text-sm py-2"
		role="combobox"
		autocomplete="off"
		aria-controls="options"
		aria-expanded="false"
	/>
	<button
		type="button"
		on:click|stopPropagation={startSearching}
		class="absolute inset-y-0 right-0 flex items-center rounded-r-md px-2 focus:outline-none"
	>
		<SelectorIcon />
	</button>
	{#if searching}
		<ul
			class="absolute z-50 mt-1 max-h-60 w-full overflow-auto divide-gray-100 divide-y rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm"
		>
			{#each filteredInOptions as option, index}
				<li
					on:click={selectOption}
					class="relative cursor-default select-none py-2 pl-8 pr-4 text-gray-600 hover:bg-gray-200 hover:text-gray-800"
					id={'in-option-' + index}
					role="option"
					tabindex="-1"
				>
					<span class="block text-left pl-4 truncate">{option}</span>
					<span class="absolute inset-y-0 left-0 flex items-center pl-1.5 text-sky-500">
						<CheckIcon />
					</span>
				</li>
			{/each}
			{#if filteredOutOptions.length > 0}
				{#each filteredOutOptions as option, index}
					<li
						on:click={selectOption}
						class="relative cursor-default select-none py-2 pl-8 pr-4 text-gray-400 hover:bg-gray-200 hover:text-gray-800"
						id={'out-option-' + index}
						role="option"
						tabindex="-1"
					>
						<span class="block text-left pl-4 truncate">{option}</span>
						<span class="absolute inset-y-0 left-0 flex items-center pl-1.5 text-gray-500">
							<CheckIcon />
						</span>
					</li>
				{/each}
			{/if}
		</ul>
	{/if}
</div>
