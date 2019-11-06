var page = new WebPage()


var c = {
    'name': 'fine_auth_token',
    'value': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmYW5ydWFuIiwiaWF0IjoxNTczMDIwMjk4LCJleHAiOjE1NzMwMjM4OTgsInN1YiI6ImFkbWluIiwiZGVzY3JpcHRpb24iOiJhZG1pbihhZG1pbikiLCJqdGkiOiJqd3QifQ.7_QPS0I5NO4G8y9bzZVs9Gf_nuK57ieaWJnACO6HukU',
    'path': '/',
    'domain':'172.23.43.13'
}
phantom.addCookie(c)

var c2 = {
    'name': 'fine_remember_login',
    'value': '-2',
    'path': '/',
    'domain':'172.23.43.13'
}
phantom.addCookie(c2)

var url = 'http://172.23.43.13:8081/webroot/decision/view/report?viewlet=report/zgpt_report/%E5%8F%91%E5%8D%A1%E7%BB%9F%E8%AE%A1.frm'

page.open(url, function (status) {


    page.viewportSize = {
        width : 1920,
        height : 1080
    }

    setTimeout(function(){
        page.render('card.jpg', {quality: 100})
        // page.render('card.png')
        // page.render('card.pdf')
        // page.render('card.bmp')
        console.log('ok')
        phantom.exit()
    }, 10000)
})

