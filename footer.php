<footer class="footer">
    <div class="wrapper">
        <div class="footer_main row">
            <div class="col xs-3">
                <div id="contacts" class="adress">
                    <b>Адреса</b><br/>
                    Ужгород, вул. Рилеєва, 4<br/>
                    <br/>
                    <b>Контакти</b><br/>
                    Email: kompot.uz.ua@gmail.com<br/>
                    Тел.: +38 095 589 46 46,<br/>
                    +38 098 589 46 46<br/>
                    <b>Телефонувати</b><br/>
                    Понеділок - П`ятниця<br/>
                    з 10:00 до 18:00<br/>
                    Субота з 10:00 до 13:00<br/>
                    SMS та Email - цілодобово<br/>
                </div>
            </div>
            <div class="col xs-3">
                        <a href="#win1" class="btn btn-primary">Замовити дзвінок</a>
                        <a href="#win2" class="btn btn-primary">Замовити підключення</a>
                <a class="btn btn-social" title="Facebook" target="_blank" href="https://www.facebook.com/KompotISP/?fref=ts"><i class="socicon socicon-facebook"></i></a>
                <a href="#x" class="overlay" id="win1"></a>
                <div class="popup">
                    <form id="free-call-form" name="freeCall" method="post" action="">
                        <div class="col">
                            <h1>Надішліть нам номер Вашого телефону i ми передзвонимо!</h1>
                            <h2 class="aligncenter" id="results"></h2>
                            <div class="row">
                                <label for="name1">Ваше ім'я *</label>
                                <input name="call-name" type="text" id="name1" placeholder="Ім'я" required>
                            </div>
                            <div class="row">
                                <label for="phonenumber">Ваш телефон *</label>
                                <input name="phonenumber" type="text" value="" placeholder="+380" id="phone" required>
                            </div>
                            <div class="row">
                                <input type="submit" name="submit" id="btn" class="btn" value="Надіслати">
                            </div>
                        </div>
                    </form>
                    <a class="close" title="Закрыть" href="#close"></a>
                </div>
                <a href="#x" class="overlay" id="win2"></a>
                <div class="popup">
                    <form id="free-order-form" name="freeOrder" method="post" action="">
                        <div class="col">
                            <h1>Надішліть нам повідомлення і ми зв'яжемось з Вами.</h1>
                            <h2 class="aligncenter" id="response"></h2>
                            <div class="row">
                                <label for="name">Ваше ім'я*</label>
                                <input name="call-name" id="name" type="text" required>

                                <label for="email">Ваш Email*</label>
                                <input name="email" id="email" type="email" required>
                            </div>
                            <div class="row">
                                <label for="phone">Ваш телефон*</label>
                                <input name="phone" id="phone" type="text" required>

                                <label for="street">Вулиця*</label>
                                <input name="street" id="street" type="text" required>
                            </div>
                            <div class="row">
                                <label for="number">№ будинку*</label>
                                <input name="number" id="number" type="text" required>

                                <label for="app">№ квартири</label>
                                <input name="app" id="app" type="text">
                            </div>
                            <br>
                            <label for="message">Ваше повідомлення</label>
                            <textarea id="message" rows="4" cols="50" name="message" form="free-order-form"></textarea>
                            <div class="row">
                                <input type="submit" name="submit" class="btn" value="Надіслати">
                            </div>
                        </div>
                    </form>
                    <a class="close" title="Закрыть" href="#close"></a>
                </div>
            </div>
            <div class="col xs-3">
                <div class="map">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d5274.035227087525!2d22.27243!3d48.628645!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4739184425c85de1%3A0x6ac38631959897e8!2sRyljejeva+St%2C+4%2C+Uzhhorod%2C+Zakarpats&#39;ka+oblast%2C+Ukraine%2C+88000!5e0!3m2!1sen!2sus!4v1558356613140!5m2!1sen!2sus"
                            width="400" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
    <div class="copyright">
        <p class="bypostauthor">Copyright (c) 2019 ISP Компот.</p>
    </div>
</footer>
<!---->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="<?= get_template_directory_uri(); ?>/ajax.js"></script>
<script src="<?= get_template_directory_uri(); ?>/public/js/script.js"></script>

<?php wp_footer(); ?>

</body>
</html>
