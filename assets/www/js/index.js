//weui.searchBar('#searchBar');
debug = false;
questionData = null;
nowQuestion = 0;
score = 0;
function debuger(x){
    if(debug)
    console.log(x);
    }
function calcScore(){
    $("#scorePanel").text('You get '+score + ' goals of '+nowQuestion+' questions!')
    score=0
    }
function turnPageOn(page){ 
    $("div[name='page']").hide();
    $(page).show();
    }
function turnTabLabelActive(tabid){
  $("a[name='tabbar_label']").removeAttr('class');
  $("a[name='tabbar_label']").attr('class','weui-tabbar__item');
  $(tabid).attr('class','weui-tabbar__item weui-bar__item_on');
}
function goToTestPage(id){
	$('#loadingToast').show()
        debuger("loading "+ id);
        //$('#page4').text('');
        $.ajax({
            url:'http://localhost:5000/titles/'+id+'/',
            success:function(data,status,xhr
        ){
            debuger(questionData)
              questionData=eval(data);
              debuger('evaled'+questionData)
              turnPageOn('#page4');
                debuger('g1'+questionData)
                generateQuestions(0);
                $('#loadingToast').hide()
        }
        
        });

        }
function checkAnswerDx(qid){
    alist = []
    tmp=true
    j=0
    for(i in $("#qtypedx input.weui-check")){
        if($("#qtypedx input.weui-check")[i].checked){alist.push(j)}
        j=j+1
    }
    rightA = eval(questionData[qid].answer)
    if(alist.length==rightA.length){
        for(i in rightA){

            if(!alist.includes(rightA[i])){ tmp=false;debuger('Wrong answer ')}
        }
        
    }else{
        tmp=false
        }
    if(tmp){
        score = score+1
        debuger('add score,now : ' + score);
        generateQuestions(nowQuestion+1)
        }else{
			for(i in $("#qtypedx input.weui-check")){
				$("#qtypedx input.weui-check")[i].checked=false
				}
			for(i in rightA){
				$("#qtypedx input.weui-check")[rightA[i]].checked=true;
				$("#wrongAnswer").show();				
				}
				setTimeout(function(){$("#wrongAnswer").hide();generateQuestions(nowQuestion+1)},1500);
		}
    }
function checkAnswerPd(qid){
    alist = []
    tmp=true
    j=0
    for(i in $("#qtypepd input.weui-check")){
        if($("#qtypepd input.weui-check")[i].checked){alist.push(j)}
        j=j+1
    }
    rightA = eval(questionData[qid].answer)
    if(alist.length==rightA.length){
        for(i in rightA){

            if(!alist.includes(rightA[i])){ tmp=false;debuger('Wrong answer ')}
        }
    }else{
        tmp=false
        }
    if(tmp){
        score = score+1
        debuger('add score,now : ' + score);
        generateQuestions(nowQuestion+1)
        }else{
			for(i in $("#qtypepd input.weui-check")){
				$("#qtypepd input.weui-check")[i].checked=false
				}
			for(i in rightA){
				$("#qtypepd input.weui-check")[rightA[i]].checked=true;	
				$("#wrongAnswer").show();			
				}
				setTimeout(function(){$("#wrongAnswer").hide();generateQuestions(nowQuestion+1)},1500);
		}
    }
function generateQuestions(qid){
    nowQuestion = qid
    if( qid > questionData.length-1){
        turnPageOn('#page5');
        calcScore();
        nowQuestion=0
        return 0;
    }
    $('.weui-progress__inner-bar').width(qid/questionData.length * 100+ '%');
    question = questionData[qid]
    chooses = eval(question.chooses)
    answer = eval(question.answer)
    if(question.qtype=='dx'){
        $("div[name='qtype']").hide()
        $("#qtypedx").show();
        $('#qtypedx div.weui-cells__title').text(question.questiontext)
        $('#qtypedx div.weui-cells').text('')
        for(i in chooses){
            res = '<label class="weui-animate-slide-up weui-cell weui-check__label" for="a'+i+'">'+
                        '<div class="weui-cell__hd">'+
                            '<input type="checkbox" class="weui-check" name="checkbox1" id="a'+i+'" value="'+i+'">'+
                            '<i class="weui-icon-checked"></i>'+
                        '</div>'+
                        '<div class="weui-cell__bd">'+
                            '<p>'+chooses[i]+'</p>'+
                        '</div>'+
                    '</label>'
            $('#qtypedx div.weui-cells').append(res)
        }
        }
        
    if(question.qtype=='pd'){
                $("div[name='qtype']").hide()
        $("#qtypepd").show();
        $('#qtypepd div.weui-cells__title').text(question.questiontext)
        }
        
    }
$(function(){
	setTimeout(function(){$('#flashscreen').hide()},2000);
	$('#loadingToast').show()
    $.ajax({
    url:'http://localhost:5000/titles/',
    success:function(data,status,xhr
    ){
        data=eval(data)
        for( i in data){      
        res='<a class="weui-cell weui-cell_access" href="javascript:goToTestPage('+data[i].id+');">'+
        ' <div class="weui-cell__bd"><p>'+data[i].title+'</p> '+
        '</div> <div class="weui-cell__ft">135人答题</div></a>'
        $("#page1 div.weui-cells").append(res)
        $('#loadingToast').hide()
    }
        }
        })
    })
