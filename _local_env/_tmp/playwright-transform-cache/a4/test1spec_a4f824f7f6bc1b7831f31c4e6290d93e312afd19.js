"use strict";

var _test = require("@playwright/test");
(0, _test.test)('test', async ({
  page
}) => {
  await page.goto('https://github.com/nyanko111777');
  await page.getByRole('link', {
    name: 'VS_Code_setting_myao',
    exact: true
  }).click();
});
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJuYW1lcyI6WyJfdGVzdCIsInJlcXVpcmUiLCJ0ZXN0IiwicGFnZSIsImdvdG8iLCJnZXRCeVJvbGUiLCJuYW1lIiwiZXhhY3QiLCJjbGljayJdLCJzb3VyY2VzIjpbInRlc3QtMS5zcGVjLnRzIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IHRlc3QsIGV4cGVjdCB9IGZyb20gJ0BwbGF5d3JpZ2h0L3Rlc3QnO1xuXG50ZXN0KCd0ZXN0JywgYXN5bmMgKHsgcGFnZSB9KSA9PiB7XG4gIGF3YWl0IHBhZ2UuZ290bygnaHR0cHM6Ly9naXRodWIuY29tL255YW5rbzExMTc3NycpO1xuICBhd2FpdCBwYWdlLmdldEJ5Um9sZSgnbGluaycsIHsgbmFtZTogJ1ZTX0NvZGVfc2V0dGluZ19teWFvJywgZXhhY3Q6IHRydWUgfSkuY2xpY2soKTtcbn0pOyJdLCJtYXBwaW5ncyI6Ijs7QUFBQSxJQUFBQSxLQUFBLEdBQUFDLE9BQUE7QUFFQSxJQUFBQyxVQUFJLEVBQUMsTUFBTSxFQUFFLE9BQU87RUFBRUM7QUFBSyxDQUFDLEtBQUs7RUFDL0IsTUFBTUEsSUFBSSxDQUFDQyxJQUFJLENBQUMsaUNBQWlDLENBQUM7RUFDbEQsTUFBTUQsSUFBSSxDQUFDRSxTQUFTLENBQUMsTUFBTSxFQUFFO0lBQUVDLElBQUksRUFBRSxzQkFBc0I7SUFBRUMsS0FBSyxFQUFFO0VBQUssQ0FBQyxDQUFDLENBQUNDLEtBQUssQ0FBQyxDQUFDO0FBQ3JGLENBQUMsQ0FBQyIsImlnbm9yZUxpc3QiOltdfQ==