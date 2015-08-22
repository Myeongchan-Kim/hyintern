<?
/*food_page.php*/
function ul_foodlist(){
	$str = "";
	$str_ul ="
	<ul data-role=\"listview\" data-split-icon=\"phone\" data-split-theme=\"a\" data-inset=\"true\">
	";
	$str_ul_end="</ul>";
	$str.=$str_ul;
	$str_li = li_foodshop("복성원", "중화요리", "02222971900");
	$str=$str.$str_li;
	$str_li = li_foodshop("청나라", "중화요리", "0222913737");
	$str=$str.$str_li;
	$str_li = li_foodshop("한양반점", "중화요리", "0222920345");
	$str=$str.$str_li;
	$str_li = li_foodshop("금룡", "중화요리", "0222937373");
	$str=$str.$str_li;
	$str_li = li_foodshop("호남식당", "닭도리탕", "0222938113");
	$str=$str.$str_li;
	$str_li = li_foodshop("동해해물탕", "해물탕", "0222318617");
	$str=$str.$str_li;
	$str_li = li_foodshop("속초해물탕", "해물탕", "0222964257");
	$str=$str.$str_li;
	$str_li = li_foodshop("설옥", "냉면", "0222919292");
	$str=$str.$str_li;
	$str_li = li_foodshop("그때그집", "?", "0222944204");
	$str=$str.$str_li;
	$str_li = li_foodshop("다원", "볶음밥", "0222993011");
	$str=$str.$str_li;
	$str_li = li_foodshop("예광촌", "?", "0222816812");
	$str=$str.$str_li;
	$str_li = li_foodshop("본죽", "죽", "0222960545");
	$str=$str.$str_li;
	$str.=$str_ul_end;
	return $str;
}

function li_foodshop($name, $dscp, $ph_num){
	$str_shop= "<li><a href=\"#notyet\" class=\"ui-icon-delete \" data-rel=\"dialog\"><h2>{$name}</h2><p>{$dscp}</p></a>";
	$str_tel= "<a href=\"tel:{$ph_num}\" >전화걸기</a></li>\n";
	$str=$str_shop.$str_tel;
	return $str;
}
?>
<div data-role='page' id='food'>
	<?
    /* 나중에 이렇게 바꾸자.
    echo header();
    echo content();
    echo footer();
    */
    ?>
	<?include 'header.php';?>
    <div data-role="content">
    	<h2>밥집</h2>
        <ul data-role="listview">
        	<li><a href="#food_s"  class="ui-btn ui-shadow ui-corner-all ui-btn-icon-right ui-icon-arrow-r">서울</a></li>
            <li><a href="#food_g" class="ui-btn ui-shadow ui-corner-all ui-btn-icon-right ui-icon-arrow-r">구리</a></li>
            <li><a href="#notyet" class="ui-btn ui-icon-delete ui-btn-icon-left" data-rel="dialog">창원</a></li>
            <li><a href="#notyet" class="ui-btn ui-icon-delete ui-btn-icon-left" data-rel="dialog">강릉</a></li>
            <li><a href="#notyet" class="ui-btn ui-icon-delete ui-btn-icon-left" data-rel="dialog">제주</a></li>
        </ul>
    </div>
	<?include 'footer.php';?>
</div><!--page food-->
<div data-role="page" id="food_s">
	<?include 'header.php';?>
    <div data-role="content">
<?
echo ul_foodlist();
?>
    </div>
	<?include 'footer.php';?>
</div>