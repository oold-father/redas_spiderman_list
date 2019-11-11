const puppeteer = require('puppeteer');

var arguments = process.argv.splice(2);

function message(code, message, data){
    result = {
        "code": code,
        "message": message,
        "data": data
    }
    return result;
}

function startCrawl(url) {
    (async () => {
        const browser = await puppeteer.launch({
            // headless: false,
            slowMo: 200
        });

        const page = await browser.newPage();

        // 删除chromium的webdriver
        await page.evaluateOnNewDocument(() => {
            delete navigator.__proto__.webdriver;
        });

        // 设置HTTP头，对整个请求过程的所有子页面有效
        page.setExtraHTTPHeaders({
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        });

        // 修改UA，这种方式设置，在HTTP头中会是大写的：'User-Agent'
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36');

        var sendSingle = 1;
        try {
            await page.goto(url);
        } catch (error) {
            var msg = message("error", "浏览器访问错误", "")
            console.log(msg);
            // console.log("\n", error);
            sendSingle = 0;
            browser.close();
        }

        if (1 == sendSingle) {
            var result = await page.content();
//            var resultBase64 = new Buffer.from(result).toString('base64');
            var msg = message("success", "爬取完成", result)
            console.log(JSON.stringify(msg));
        }
        browser.close();
    })();
};

startCrawl(arguments[0]);