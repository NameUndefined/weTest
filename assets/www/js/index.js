weui.searchBar('#searchBar');
debug = false;
questionData = null;
nowQuestion = 0;
score = 0;
trans = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',
            'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8};
SERVER_IP = 'http://township.ink:8001';
//SERVER_IP = 'http://localhost:5000';

function debuger(x) {
    if (debug)
        console.log(x);
}

function calcScore() {
    $("#scorePanel").text('你得到了 ' + score + ' 分 '); //+ nowQuestion + ' questions!');
    score = 0;
}

function turnPageOn(page) {
    $("div[name='page']").hide();
    $(page).show();
}

function turnTabLabelActive(tabid) {
    $("a[name='tabbar_label']").removeAttr('class');
    $("a[name='tabbar_label']").attr('class', 'weui-tabbar__item');
    $(tabid).attr('class', 'weui-tabbar__item weui-bar__item_on');
}

function goToTestPage(id) {
    $('#loadingToast').show();
    debuger("loading " + id);
    //$('#page4').text('');
    $.ajax({
        url: SERVER_IP + '/titles/' + id + '/',
        success: function (data, status, xhr) {
            debuger(questionData);
            questionData = eval(data);
            debuger('evaled' + questionData);
            turnPageOn('#page4');
            debuger('g1' + questionData);
            generateQuestions(0);
            $('#loadingToast').hide();
        }

    });

}

function checkAnswerDx(qid) {
    alist = [];
    tmp = true;
    j = 0
    for (i in $("#qtypedx input.weui-check")) {
        if ($("#qtypedx input.weui-check")[i].checked) {
            alist.push(trans[j]);
        }
        j = j + 1;
    }
    rightA = eval(questionData[qid].answer);
    if (alist.length == rightA.length) {
        for (i in rightA) {

            if (!alist.includes(rightA[i])) {
                tmp = false;
                debuger('Wrong answer ');
            }
        }

    } else {
        tmp = false;
    }
    if (tmp) {
        score = score + 1;
        debuger('add score,now : ' + score);
        generateQuestions(nowQuestion + 1);
    } else {
        for (i in $("#qtypedx input.weui-check")) {
            $("#qtypedx input.weui-check")[i].checked = false;
        }
        for (i in rightA) {
            $("#qtypedx input.weui-check")[trans[rightA[i]]].checked = true;
            //$("#qtypedx input.weui-check :eq(1)").animateCss('lightSpeedIn');
            weui.topTips('答错啦', 500);
        }
        setTimeout(function () {

                generateQuestions(nowQuestion + 1);
            },
            1500);
    }
}

function checkAnswerPd(qid) {
    alist = [];
    tmp = true;
    j = 0;
    for (i in $("#qtypepd input.weui-check")) {
        if ($("#qtypepd input.weui-check")[i].checked) {
            alist.push(j?0:1);
        }
        j = j + 1;
    }
    rightA = eval(questionData[qid].answer);
    if (alist.length == rightA.length) {
        for (i in rightA) {

            if (!alist.includes(rightA[i])) {
                tmp = false;
                debuger('Wrong answer ');
            }
        }
    } else {
        tmp = false;
    }
    if (tmp) {
        score = score + 1;

        debuger('add score,now : ' + score);
        generateQuestions(nowQuestion + 1);
    } else {
        for (i in $("#qtypepd input.weui-check")) {
            $("#qtypepd input.weui-check")[i].checked = false;
        }
        for (i in rightA) {
            $("#qtypepd input.weui-check")[rightA[i]].checked = true;
            weui.topTips('答错啦', 500);
        }
        setTimeout(function () {

                generateQuestions(nowQuestion + 1);
            },
            1500);
    }
}

function generateQuestions(qid) {
    nowQuestion = qid;
    if (qid > questionData.length - 1) {
        turnPageOn('#page5');
        calcScore();
        nowQuestion = 0;
        return 0;
    }
    $('.weui-progress__inner-bar').width(qid / questionData.length * 100 + '%');
    question = questionData[qid];
    chooses = eval(question.chooses);
    answer = eval(question.answer);
    if (question.qtype == 'dx') {
        $("div[name='qtype']").hide();
        $("#qtypedx").show();
        $('#qtypedx div.weui-cells__title').text(question.questiontext);
        $('#qtypedx div.weui-cells').text('');
        for (i in chooses) {
            res = '<label class="weui-animate-slide-up weui-cell weui-check__label" for="a' + i + '">' +
                '<div class="weui-cell__hd">' + '<input type="checkbox" class="weui-check" name="checkbox1" id="a' + i +
                '" value="' + i + '">' + '<i class="weui-icon-checked"></i>' + '</div>' + '<div class="weui-cell__bd">' +
                '<p>' + chooses[i] + '</p>' + '</div>' + '</label>';
            $('#qtypedx div.weui-cells').append(res);
        }
    }

    if (question.qtype == 'pd') {
        $("div[name='qtype']").hide();
        $("#qtypepd").show();
        $('#qtypepd div.weui-cells__title').text(question.questiontext);
    }

}
$(function () {
    //setTimeout(function() {
    //    $('#flashscreen').hide();
    //},
    //2000);
    //var vConsole = new VConsole();
    $.fn.extend({
        animateCss: function (animationName, callback) {
            var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            this.addClass('animated ' + animationName).one(animationEnd, function () {
                $(this).removeClass('animated ' + animationName);
                if (callback) {
                    callback();
                }
            });
            return this;
        }
    });
    $('#loadingToast').show();
    $.ajax({
        url: SERVER_IP + '/titles/',
        success: function (data, status, xhr) {
            data = eval(data);
            for (i in data) {
                res = '<a class="weui-cell weui-cell_access" href="javascript:goToTestPage(' + data[i].id + ');">' +
                    ' <div class="weui-cell__bd"><p>' + data[i].title + '</p> ' +
                    '</div> <div class="weui-cell__ft">135人答题</div></a>';
                $("#page1 div.weui-cells").append(res);
                $('#loadingToast').hide();
            }
        }
    });
});