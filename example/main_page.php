<?
/*main_page.php*/
?>
<div data-role='page' id='front'>
	<?
    /* 나중에 이렇게 바꾸자.
    echo header();
    echo content();
    echo footer();
    */
    ?>
    <div data-role="header">
     	<h1>HY인턴꿀</h1>
    </div>
    <div data-role="content">
    	<h2>메인메뉴</h2>
        <ul data-role="listview">
        	<li><a href="#food" class="ui-btn">밥집</a></li>
            <li><a href="#notyet" class="ui-btn ui-icon-delete ui-btn-icon-left" data-rel="dialog">술기팁</a></li>
            <li><a href="#notyet" class="ui-btn ui-icon-delete ui-btn-icon-left" data-rel="dialog">기타</a></li>
        </ul>
    </div>
    <div data-role="footer">
    	<h2>2014 COPYRIGHT &copy; 김명찬</h2>
    </div>
</div><!--page-->
