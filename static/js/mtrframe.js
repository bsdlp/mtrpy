/* var mtrFrameCSS = document.createElement("link")
mtrFrameCSS.href = "/static/css/style.css";
mtrFrameCSS .rel = "stylesheet";
mtrFrameCSS .type = "text/css";
frames['mtrWINDOW'].document.body.appendChild(mtrFrameCSS); */

$(document).ready(function());
    {
        // Set specific variable to represent all iframe tags.
        var iFrames = $(".mtrWINDOW");

        // Resize heights.
        function mtrResizeFrame()
        {
            $(".mtrWINDOW").style.height = $(".mtrWINDOW").contentWindow.document.body.offsetHeight + 'px';
        }

        // Check if browser is Safari or Opera.
        if ($.browser.safari || $.browser.opera)
        {
            // Start timer when loaded.
            $('iframe').load(function()
                {
                    setTimeout(mtrResizeFrame, 0);
                }
            );

            // Safari and Opera need a kick-start.
            var mtrFrameSource = $(".mtrWINDOW").src;
            $(".mtrWINDOW").src = '';
            $(".mtrWINDOW").src = mtrFrameSource;
        }
        else
        {
            // For other good browsers.
            $('iframe').load(function()
                {
                    // Set inline style to equal the body height of the iframed content.
                    this.style.height = this.contentWindow.document.body.offsetHeight + 'px';
                }
            );
        }
    }
