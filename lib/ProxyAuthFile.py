import zipfile

class ProxyCode:

    proxy_server_host = ""
    port = ""
    user = ""
    pw = ""

    def __init__(self, proxy_server_host, port, user, pw):
        self.proxy_server_host = proxy_server_host
        self.port = port
        self.user = user
        self.pw = pw

    def createZip(self, path):
        with zipfile.ZipFile(path, 'w') as zp:
            zp.writestr("manifest.json", self.get_manifest_json())
            zp.writestr("background.js", self.get_background_js())

    def get_manifest_json(self):
        return """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

    def get_background_js(self):
        return """
        var config = {
                mode: "fixed_servers",
                rules: {
                  singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                  },
                  bypassList: []
                }
              };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (self.proxy_server_host, self.port, self.user, self.pw)
