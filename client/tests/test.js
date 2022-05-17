import { expect, test } from '@playwright/test';

test('new image modal shown when button clicked', async ({ page }) => {
	await page.locator('#newImageButton').click();

	const modal = await page.locator('#newImageModal');
	expect(modal).toBeVisible();
});
