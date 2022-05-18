import { expect, test } from '@playwright/test';

test('adding a PNG is successful', async ({ page, request }) => {
	await page.goto('/');

	await page.locator("button.open-modal").click();

	await page.type("form.new-image-form .file-input", '../assets.100x400.png');

	await page.locator("#newImageForm .save-image").click();

	expect(request.failure().errorText).toBe(false);
});
