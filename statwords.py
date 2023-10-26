class StatusWords:
    def __init__(self, word=None, value=None):
        self.content = {
            "aborted"      : {"title": "Aborted", "icon": "⛔️"},
            "cancelled"    : {"title": "Cancelled", "icon": "❌"},
            "cleaning"     : {"title": "Cleaning", "icon": "🧹"},
            "compiling"    : {"title": "Compiling", "icon": "🔨"},
            "complete"     : {"title": "Complete", "icon": "✅"},
            "connecting"   : {"title": "Connecting", "icon": "🔗"},
            "deleting"     : {"title": "Deleting", "icon": "🗑"},
            "disconnecting": {"title": "Disconnecting", "icon": "🔌"},
            "downloading"  : {"title": "Downloading", "icon": "⬇️"},
            "error"        : {"title": "Error", "icon": "❗️"},
            "exporting"    : {"title": "Exporting", "icon": "📤"},
            "failure"      : {"title": "Failure", "icon": "❌"},
            "finished"     : {"title": "Finished", "icon": "🎉"},
            "idle"         : {"title": "Idle", "icon": "🕛"},
            "importing"    : {"title": "Importing", "icon": "📥"},
            "installing"   : {"title": "Installing", "icon": "🔧"},
            "loading"      : {"title": "Loading", "icon": "⏳"},
            "paused"       : {"title": "Paused", "icon": "⏸"},
            "pending"      : {"title": "Pending", "icon": "🕒"},
            "progress"     : {"title": "Progress", "icon": "🔄"},
            "receiving"    : {"title": "Receiving", "icon": "📩"},
            "refreshing"   : {"title": "Refreshing", "icon": "🔄"},
            "rendering"    : {"title": "Rendering", "icon": "🎨"},
            "restarting"   : {"title": "Restarting", "icon": "🔄"},
            "resuming"     : {"title": "Resuming", "icon": "▶️"},
            "running"      : {"title": "Running", "icon": "🏃"},
            "saving"       : {"title": "Saving", "icon": "💾"},
            "scanning"     : {"title": "Scanning", "icon": "🔍"},
            "sending"      : {"title": "Sending", "icon": "📤"},
            "size"         : {"title": "Size", "icon": "📐"},
            "started"      : {"title": "Started", "icon": "🚀"},
            "success"      : {"title": "Success", "icon": "✅"},
            "syncing"      : {"title": "Syncing", "icon": "🔄"},
            "uninstalling" : {"title": "Uninstalling", "icon": "🔧"},
            "updating"     : {"title": "Updating", "icon": "🔃"},
            "uploading"    : {"title": "Uploading", "icon": "⬆️"},
            "validating"   : {"title": "Validating", "icon": "✅"},
            "verifying"    : {"title": "Verifying", "icon": "✅"},
            "waiting"      : {"title": "Waiting", "icon": "⌛️"},
        }
        self.display = {"status": "", "value": ""}
        self.set(word or "", value)

    def set(self, word: str, value=None):
        """
        outtputto display: an icon and status word, as well as the state if exists
        """
        if word in self.content:
            self.display["status"] = f"{ self.content[word]['icon']} {self.content[word]['title']}"
        else:
            self.display["status"] = word or ""

        if value in self.content:
            self.display["value"] = f"{ self.content[str(value)]['title']}"
        else:
            self.display["value"] = str(value)
        return self.display



    def response_code(self, code):
        """
        Returns the HTTP response code as a string representation.
        """
        response_codes = {
            100: "Continue",
            101: "Switching Protocols",
            102: "Processing",
            103: "Early Hints",
            200: "OK",
            201: "Created",
            202: "Accepted",
            203: "Non-Authoritative Information",
            204: "No Content",
            205: "Reset Content",
            206: "Partial Content",
            207: "Multi-Status",
            208: "Already Reported",
            226: "IM Used",
            300: "Multiple Choice",
            301: "Moved Permanently",
            302: "Found",
            303: "See Other",
            304: "Not Modified",
            305: "Use Proxy",
            307: "Temporary Redirect",
            308: "Permanent Redirect",
            400: "Bad Request",
            401: "Unauthorized",
            402: "Payment Required",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            406: "Not Acceptable",
            407: "Proxy Authentication Required",
            408: "Request Timeout",
            409: "Conflict",
            410: "Gone",
            411: "Length Required",
            412: "Precondition Failed",
            413: "Payload Too Large",
            414: "URI Too Long",
            415: "Unsupported Media Type",
            416: "Range Not Satisfiable",
            417: "Expectation Failed",
            418: "I'm a teapot",
            421: "Misdirected Request",
            422: "Unprocessable Entity",
            423: "Locked",
            424: "Failed Dependency",
            425: "Too Early",
            426: "Upgrade Required",
            428: "Precondition Required",
            429: "Too Many Requests",
            431: "Request Header Fields Too Large",
            451: "Unavailable For Legal Reasons",
            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
            504: "Gateway Timeout",
            505: "HTTP Version Not Supported",
            506: "Variant Also Negotiates",
            507: "Insufficient Storage",
            508: "Loop Detected",
            510: "Not Extended",
            511: "Network Authentication Required",
        }

        if code in response_codes:
            self.display['status'] = 'HTTP Respopnse Code'
            self.display['value']  = response_codes[code]
        else:
            return "Unknown"
