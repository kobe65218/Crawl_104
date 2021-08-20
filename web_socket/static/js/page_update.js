

$("#button").click(
    function () {
        var page_last = 0
        var page_now = 0
        var time = 0
        var page_toatal = 0

        var socket = io.connect("http://"+ "kobe655218.ddns.net" + ':' + "9091/test");
        var socket2 = io.connect("http://"+ "kobe655218.ddns.net" + ':' + "9091/crawl");

        socket.on('connect', function (msg) {
            socket.emit('my_event', {"data": "test"})
        });

        socket.on('message', function (msg) {
            console.log(msg)
        })


        socket2.on('total_page', function (msg) {
            $("span#total").html(msg["page"])
            page_toatal = msg['page']
        })

        socket2.on('response2', function (msg) {
            page_now = parseInt(msg["page"])
            $("span#current").html(msg["page"])

            if (page_now == page_toatal){
                clearInterval(timer)
                $("span#remain-time").html("finish")

            }
        })

        var timer = setInterval(() => {
            var divPage = parseInt(page_now) - parseInt(page_last)
            window["chart"].data.datasets[0].data.push(divPage)
            console.log(window["chart"].data.labels)
            var array = window["chart"].data.labels
            window["chart"].data.labels.push(parseInt(array[array.length-1])+10)
            window["chart"].update()

            var remain_time = (page_toatal - page_now)/divPage*10
            $("span#remain-time").html(remain_time.toFixed(2) + " s")
            page_last = page_now
            time += 10
        },
            10000

        )

    })



