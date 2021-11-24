title = """<meta id="OGTitle" property="og:title" content="SeleniumBase">
    <title>Test Report</title>
    <link rel="SHORTCUT ICON"
    href="https://seleniumbase.io/img/favicon.ico" /> """

style = (
    title
    + """<style type="text/css">
    html {
        background-color: #9988ad;
    }
    html, body {
        font-size: 100%;
        box-sizing: border-box;
    }
    body {
        background-image: none;
        background-origin: padding-box;
        background-color: #c6d6f0;
        padding: 30;
        margin: 10;
        font-family: "Proxima Nova","proxima-nova",
        "Helvetica Neue",Helvetica,Arial,sans-serif !important;
        text-rendering: optimizelegibility;
        -moz-osx-font-smoothing: grayscale;
        box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.24),
        1px 2px 12px 0px rgba(0, 0, 0, 0.18) !important;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        border-spacing: 0;
        box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.27),
        1px 2px 12px 0px rgba(0, 0, 0, 0.21) !important;
        transition: all 0.15s ease-out 0s;
        transition-property: all;
        transition-duration: 0.1s;
        transition-timing-function: ease-out;
        transition-delay: 0s;
    }
    table:hover {
        box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.35),
        1px 2px 12px 0px rgba(0, 0, 0, 0.28) !important;
    }
    thead th, thead td {
        padding: 0.5rem 0.625rem 0.625rem;
        font-weight: bold;
        text-align: left;
    }
    thead {
        text-align: center;
        border: 1px solid #e1e1e1;
        width: 150%;
        color: #0C8CDF;
        background-color: #c0f0ff;
    }
    tbody tr:nth-child(even) {
        background-color: #f1f1f1;
    }
    tbody tr:nth-child(odd) {
        background-color: #ffffff;
    }
    tbody tr:nth-child(even):hover {
        background-color: #f8f8d2;
    }
    tbody tr:nth-child(odd):hover {
        background-color: #ffffe0;
    }
    tbody th, tbody td {
        padding: 0.5rem 0.625rem 0.625rem;
    }
    tbody {
        border: 1px solid #e1e1e1;
        background-color: #fefefe;
    }
    td {
        padding: 5px 5px 5px 0;
        vertical-align: top;
    }
    h1 table {
        font-size: 27px;
        text-align: left;
        padding: 0.5rem 0.625rem 0.625rem;
        font-weight: bold;
        padding-right: 10px;
        padding-left: 20px;
        padding: 15px 15px 15px 0;
    }
    h2 table {
        color: #0C8CDF;
        font-size: 16px;
        text-align: left;
        font-weight: bold;
        padding: 5px 5px 5px 0;
        padding-right: 10px;
        padding-left: 20px;
    }
    </style>"""
)

# Bootstrap Tour Backdrop Style
bt_backdrop_style = """
    .tour-tour-element {
        pointer-events: none !important;
    }
    :not(.tour-tour-element) .orphan.tour-tour {
        box-shadow: 0 0 0 88422px rgba(0, 0, 0, 0.42);
        pointer-events: auto !important;
    }
    """

# DriverJS Tour Backdrop Style
dt_backdrop_style = """
    .driver-fix-stacking {
        pointer-events: none !important;
    }
    #driver-popover-item, .popover-class {
        pointer-events: auto !important;
    }
    button.driver-prev-btn.driver-disabled {
        visibility: hidden;
    }
    """

messenger_style = """
    .messenger-message-inner {
        font-family: "Proxima Nova","proxima-nova",Arial,sans-serif !important;
        font-size: 17px;
    }
    ul.messenger-theme-flat {
        box-shadow: 2px 2px 5px 2px rgba(16, 128, 120, 0.34),
        2px 2px 10px 2px rgba(16, 128, 120, 0.28) !important;
    }
    """

sh_style_test = """
    var test_tour = new Shepherd.Tour({
      defaults: {
        classes: 'shepherd-theme-dark',
        scrollTo: true
      }
    });
    """

# Hopscotch Backdrop Style
hops_backdrop_style = """
    .hopscotch-bubble-container {
        font-size: 110%;
    }
    """

# IntroJS Style
introjs_style = """
    .introjs-button.introjs-nextbutton,
    .introjs-button.introjs-donebutton {
        color: #fff !important;
        background-color: %s !important;
        border: 1px solid %s !important;
        text-shadow: none;
        box-shadow: none;
    }
    .introjs-button.introjs-nextbutton:hover,
    .introjs-button.introjs-donebutton:hover {
        color: #fff !important;
        background-color: %s !important;
        border: 1px solid %s !important;
    }
    .introjs-button {
        box-sizing: content-box;
        text-decoration: none;
    }
    .introjs-button.introjs-skipbutton {
        color: %s;
    }
    .introjs-tooltip, .introjs-floating {
        box-sizing: content-box;
        position: absolute;
    }
"""

# Shepherd Backdrop Style
sh_backdrop_style = """
    body.shepherd-active .shepherd-target.shepherd-enabled {
        box-shadow: 0 0 0 99999px rgba(0, 0, 0, 0.20);
        pointer-events: none !important;
        z-index: 9999;
    }

    body.shepherd-active .shepherd-orphan {
        box-shadow: 0 0 0 99999px rgba(0, 0, 0, 0.20);
        pointer-events: auto;
        z-index: 9999;
    }

    body.shepherd-active
        .shepherd-enabled.shepherd-element-attached-top {
            position: relative;
    }

    body.shepherd-active
        .shepherd-enabled.shepherd-element-attached-bottom {
            position: relative;
    }

    body.shepherd-active .shepherd-step {
        pointer-events: auto;
        z-index: 9999;
    }

    body.shepherd-active {
        pointer-events: none !important;
    }
    """

# pytest html-report Style
pytest_style = """
    body {
        font-family: Helvetica, Arial, sans-serif;
        font-size: 12px;
        min-width: 800px;
        color: #999;
    }
    h1 {
        font-size: 24px;
        color: black;
    }
    h2 {
        font-size: 16px;
        color: black;
    }
    p {
        color: black;
    }
    a {
        color: #999;
    }
    table {
        border-collapse: collapse;
    }
    #environment td {
        padding: 5px;
        border: 1px solid #E6E6E6;
    }
    #environment tr:nth-child(odd) {
        background-color: #f6f6f6;
    }
    span.passed, .passed .col-result {
        color: green;
    }
    span.skipped, span.xfailed, span.rerun, .skipped .col-result,
    .xfailed .col-result, .rerun .col-result {
        color: orange;
    }
    span.error, span.failed, span.xpassed, .error .col-result,
    .failed .col-result, .xpassed .col-result  {
        color: red;
    }
    #results-table {
        border: 1px solid #e6e6e6;
        color: #999;
        font-size: 12px;
        width: 100%
    }
    #results-table th, #results-table td {
        padding: 5px;
        border: 1px solid #E6E6E6;
        text-align: left
    }
    #results-table th {
        font-weight: bold
    }
    .log:only-child {
        height: inherit
    }
    .log {
        background-color: #e6e6e6;
        border: 1px solid #e6e6e6;
        color: black;
        display: block;
        font-family: "Courier New", Courier, monospace;
        height: 230px;
        overflow-y: scroll;
        padding: 5px;
        white-space: pre-wrap
    }
    div.image {
        border: 1px solid #e6e6e6;
        float: right;
        height: 240px;
        margin-left: 5px;
        overflow: hidden;
        width: 320px
    }
    div.image img {
        width: 320px
    }
    .collapsed {
        display: none;
    }
    .expander::after {
        content: " (show details)";
        color: #BBB;
        font-style: italic;
        cursor: pointer;
    }
    .collapser::after {
        content: " (hide details)";
        color: #BBB;
        font-style: italic;
        cursor: pointer;
    }
    .sortable {
        cursor: pointer;
    }
    .sort-icon {
        font-size: 0px;
        float: left;
        margin-right: 5px;
        margin-top: 5px;
        width: 0;
        height: 0;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
    }
    .inactive .sort-icon {
        border-top: 8px solid #E6E6E6;
    }
    .asc.active .sort-icon {
        border-bottom: 8px solid #999;
    }
    .desc.active .sort-icon {
        border-top: 8px solid #999;
    }
    """
