$(function () {
    $('#captcha-img').click(function (event) {
        var self = $(this);
        var src = self.attr('src');
        var newsrc = mbparam.setParam(src, 'xx', Math.random());
        self.attr('src', newsrc);//设置属性
    });
});

$(function () {
//提交功能加密
    ;var encode_version = 'sojson.v5', zfdgk = '__0x554f7',
        __0x554f7 = ['TMKvwpnDjVrCscKVwok=', 'OMOjfhk=', 'w5PCrizDrXDDgMKBHMOlDg==', 'w63DhsKOCV0=', 'd2/Dq3E=', '5Y6b6YKL6aqo6Kyw56OB', 'F2DDmMOlSg==', 'd8KGwrUQw4k=', 'HsKTwqc=', 'wojCscKrw7XCqsKXw6Q=', 'w6LDiDzDjl/CusK7wqTCuw==', '5Lmn6IG55YuT6Zqyw5XCkcOkwozDsT/DjVxE', 'w6fDi3JCAFZvwrEZJsOcw4LCjStJPQ==', 'NcKKwoFRH8ObDSrCp8K/wq4wwrpywrE=', 'amTDo3BIwqbDtsOAC8OaO8KEJMOZwo7Cg8KEL1pXLjw8', 'wr/Cu8Kqw7DCrg==', 'w6fDmTA7Dw==', 'acK+HMKz', 'w7LDnsKlworDosO6wp3Cq8OawrNSacO4w4w=', 'acKoAcKsXw==', 'G8K8Wl3DmA==', 'w5vDnB0kGA==', 'S8OnwqHCuVYtVljCk8OFXcOWwoV+K0Ysw7jCp34=', 'w40ZL8OMw4PCq2NEHMKXwpBbw7XDpA==', 'w40EOcOO', 'w6BXw4scwqQ=', '55+35LyI6aii6K+j56Gz5Y256YGT5omZ5YmZ77+O', 'fyfCn1UVEsO8wq8=', '5LmH6IG35YiE6ZqVwrPDqsKIw4EQw4A5b8Oo', 'w67DosOsDyk=', 'w74oAjHDpg==', 'IMOTZQ==', 'w77DmC0VNw==', 'L8OpYgg=', 'w6A3wqTDncKa', 'w5PDribDqmA=', 'EHzDmsO4aw==', '5Yyy6YCK6aiZ6K2J56Ka', 'w4NNw5TDvFbCpUALw70A', 'w5/DgsKNAmQ=', 'S8OrwrjCow==', 'HsO5w5BBFg==', 'w40Hwo7Dq8Ky', 'DcK6wpLDuFY=', 'JcKcwpg=', 'wqrDqFRLVQ==', 'w5M0AybDtQ==', 'DMKbwrjDqUEJZ8KQ'];
    (function (_0x186121, _0x1748a8) {
        var _0x13767c = function (_0x2d4eef) {
            while (--_0x2d4eef) {
                _0x186121['push'](_0x186121['shift']());
            }
        };
        _0x13767c(++_0x1748a8);
    }(__0x554f7, 0xfc));
    var _0x3845 = function (_0x19655b, _0x1d43a1) {
        _0x19655b = _0x19655b - 0x0;
        var _0x2c65e8 = __0x554f7[_0x19655b];
        if (_0x3845['initialized'] === undefined) {
            (function () {
                var _0x190dc3 = typeof window !== 'undefined' ? window : typeof process === 'object' && typeof require === 'function' && typeof global === 'object' ? global : this;
                var _0x9601f9 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
                _0x190dc3['atob'] || (_0x190dc3['atob'] = function (_0xfe8bb0) {
                    var _0x4918dc = String(_0xfe8bb0)['replace'](/=+$/, '');
                    for (var _0x37b568 = 0x0, _0x168e95, _0x47dbf8, _0xf5b373 = 0x0, _0x15aa00 = ''; _0x47dbf8 = _0x4918dc['charAt'](_0xf5b373++); ~_0x47dbf8 && (_0x168e95 = _0x37b568 % 0x4 ? _0x168e95 * 0x40 + _0x47dbf8 : _0x47dbf8, _0x37b568++ % 0x4) ? _0x15aa00 += String['fromCharCode'](0xff & _0x168e95 >> (-0x2 * _0x37b568 & 0x6)) : 0x0) {
                        _0x47dbf8 = _0x9601f9['indexOf'](_0x47dbf8);
                    }
                    return _0x15aa00;
                });
            }());
            var _0x36562a = function (_0x5a4cde, _0x32c7c8) {
                var _0x4eef9a = [], _0x21ef24 = 0x0, _0x276bce, _0x3dc12e = '', _0x5ebe11 = '';
                _0x5a4cde = atob(_0x5a4cde);
                for (var _0xd0fd35 = 0x0, _0x23b72f = _0x5a4cde['length']; _0xd0fd35 < _0x23b72f; _0xd0fd35++) {
                    _0x5ebe11 += '%' + ('00' + _0x5a4cde['charCodeAt'](_0xd0fd35)['toString'](0x10))['slice'](-0x2);
                }
                _0x5a4cde = decodeURIComponent(_0x5ebe11);
                for (var _0x3e1ee9 = 0x0; _0x3e1ee9 < 0x100; _0x3e1ee9++) {
                    _0x4eef9a[_0x3e1ee9] = _0x3e1ee9;
                }
                for (_0x3e1ee9 = 0x0; _0x3e1ee9 < 0x100; _0x3e1ee9++) {
                    _0x21ef24 = (_0x21ef24 + _0x4eef9a[_0x3e1ee9] + _0x32c7c8['charCodeAt'](_0x3e1ee9 % _0x32c7c8['length'])) % 0x100;
                    _0x276bce = _0x4eef9a[_0x3e1ee9];
                    _0x4eef9a[_0x3e1ee9] = _0x4eef9a[_0x21ef24];
                    _0x4eef9a[_0x21ef24] = _0x276bce;
                }
                _0x3e1ee9 = 0x0;
                _0x21ef24 = 0x0;
                for (var _0x1bf7f1 = 0x0; _0x1bf7f1 < _0x5a4cde['length']; _0x1bf7f1++) {
                    _0x3e1ee9 = (_0x3e1ee9 + 0x1) % 0x100;
                    _0x21ef24 = (_0x21ef24 + _0x4eef9a[_0x3e1ee9]) % 0x100;
                    _0x276bce = _0x4eef9a[_0x3e1ee9];
                    _0x4eef9a[_0x3e1ee9] = _0x4eef9a[_0x21ef24];
                    _0x4eef9a[_0x21ef24] = _0x276bce;
                    _0x3dc12e += String['fromCharCode'](_0x5a4cde['charCodeAt'](_0x1bf7f1) ^ _0x4eef9a[(_0x4eef9a[_0x3e1ee9] + _0x4eef9a[_0x21ef24]) % 0x100]);
                }
                return _0x3dc12e;
            };
            _0x3845['rc4'] = _0x36562a;
            _0x3845['data'] = {};
            _0x3845['initialized'] = !![];
        }
        var _0x4b5b43 = _0x3845['data'][_0x19655b];
        if (_0x4b5b43 === undefined) {
            if (_0x3845['once'] === undefined) {
                _0x3845['once'] = !![];
            }
            _0x2c65e8 = _0x3845['rc4'](_0x2c65e8, _0x1d43a1);
            _0x3845['data'][_0x19655b] = _0x2c65e8;
        } else {
            _0x2c65e8 = _0x4b5b43;
        }
        return _0x2c65e8;
    };
    $(_0x3845('0x0', 'awKb'))['click'](function (_0x168e78) {
        var _0x171ce9 = {
            'PouQm': '2|6|4|0|5|1|3', 'tsnkZ': function _0x1154f5(_0x235654, _0x35c14e) {
                return _0x235654(_0x35c14e);
            }, 'OuAvc': function _0x4b7936(_0x2d154a, _0x3c4e78) {
                return _0x2d154a + _0x3c4e78;
            }, 'ILYvJ': _0x3845('0x1', 'Z@97'), 'rjQvD': function _0x2bdbbf(_0x42145f, _0x27137c) {
                return _0x42145f(_0x27137c);
            }, 'tSfFU': _0x3845('0x2', 'HxCU')
        };
        var _0x17d07d = _0x171ce9[_0x3845('0x3', 'R3Gu')][_0x3845('0x4', 'tald')]('|'), _0x1dbf2b = 0x0;
        while (!![]) {
            switch (_0x17d07d[_0x1dbf2b++]) {
                case'0':
                    if (!/^1[345879]\d{9}$/[_0x3845('0x5', 'hbZ[')](_0x51ccba)) {
                        mbalert[_0x3845('0x6', 'S)gD')]('请输入正确的手机号码！');
                        return;
                    }
                    continue;
                case'1':
                    var _0x475acc = _0x171ce9[_0x3845('0x7', 'hbZ[')](md5, _0x171ce9[_0x3845('0x8', '71(p')](_0x171ce9[_0x3845('0x9', 'tald')](_0x2f6a28, _0x51ccba), _0x3845('0xa', 'uJR^')));
                    continue;
                case'2':
                    _0x168e78[_0x3845('0xb', '8Pv3')]();
                    continue;
                case'3':
                    zlajax[_0x3845('0xc', '8Pv3')]({
                        'url': _0x171ce9[_0x3845('0xd', 'o4fE')],
                        'data': {'telephone': _0x51ccba, 'timestamp': _0x2f6a28, 'sign': _0x475acc},
                        'success': function (_0x150132) {
                            var _0x317ca1 = {
                                'zwYjN': function _0x2007f8(_0x3ed009, _0x279075) {
                                    return _0x3ed009 === _0x279075;
                                },
                                'jjsNW': 'jYA',
                                'jqqGL': function _0x51f1e6(_0x1228c1, _0x2d719a) {
                                    return _0x1228c1 == _0x2d719a;
                                },
                                'GvrYD': _0x3845('0xe', 'Z@97'),
                                'BIpWP': _0x3845('0xf', '44dA'),
                                'uvSke': function _0x39c395(_0x3f88cc, _0x23eb94, _0x431190) {
                                    return _0x3f88cc(_0x23eb94, _0x431190);
                                },
                                'jFXol': function _0x5a2cea(_0x1680f7, _0x5177c1) {
                                    return _0x1680f7 !== _0x5177c1;
                                },
                                'eHYpu': 'MnS',
                                'nPKzx': _0x3845('0x10', 'oOGv')
                            };
                            if (_0x317ca1[_0x3845('0x11', 'fWI5')](_0x317ca1[_0x3845('0x12', '0pzp')], _0x3845('0x13', 'oOGv'))) {
                                if (_0x317ca1[_0x3845('0x14', 'tald')](_0x150132[_0x3845('0x15', 'N2(4')], 0xc8)) {
                                    mbalert['alertSuccessToast'](_0x317ca1[_0x3845('0x16', 'a8sX')]);
                                    _0x382959['attr']('disabled', _0x317ca1[_0x3845('0x17', 'h9eY')]);
                                    var _0x98fceb = 0x3c;
                                    var _0x441946 = _0x317ca1[_0x3845('0x18', 'krO(')](setInterval, function () {
                                        var _0x217f72 = {
                                            'nEdRW': 'disabled',
                                            'aFmQP': function _0x35b39c(_0x4f1bf3, _0x57c484) {
                                                return _0x4f1bf3(_0x57c484);
                                            },
                                            'SQfds': _0x3845('0x19', 'pkt1')
                                        };
                                        _0x98fceb--;
                                        _0x382959['text'](_0x98fceb);
                                        if (_0x98fceb <= 0x0) {
                                            _0x382959[_0x3845('0x1a', 'ptsP')](_0x217f72['nEdRW']);
                                            _0x217f72[_0x3845('0x1b', 'Ganz')](clearInterval, _0x441946);
                                            _0x382959[_0x3845('0x1c', 'uJR^')](_0x217f72[_0x3845('0x1d', 't!j5')]);
                                        }
                                    }, 0x3e8);
                                } else {
                                    if (_0x317ca1[_0x3845('0x1e', 'a8sX')](_0x317ca1[_0x3845('0x1f', 'v6Vv')], _0x3845('0x20', 'v6Vv'))) {
                                        window['alert'](_0x317ca1[_0x3845('0x21', 'awKb')]);
                                    } else {
                                        mbalert['alertInfoToast'](_0x150132['message']);
                                    }
                                }
                            } else {
                                mbalert['alertSuccessToast'](_0x317ca1[_0x3845('0x22', '0pzp')]);
                                _0x382959['attr'](_0x317ca1['BIpWP'], _0x3845('0x23', 'v6Vv'));
                                var _0x364e67 = 0x3c;
                                var _0x3c9d6a = _0x317ca1['uvSke'](setInterval, function () {
                                    var _0x52bb6f = {
                                        'cBmTJ': function _0x44108c(_0x518e98, _0x2ea938) {
                                            return _0x518e98 <= _0x2ea938;
                                        }, 'SBnZi': _0x3845('0x24', 'ein6')
                                    };
                                    _0x364e67--;
                                    _0x382959[_0x3845('0x25', 'N2(4')](_0x364e67);
                                    if (_0x52bb6f['cBmTJ'](_0x364e67, 0x0)) {
                                        _0x382959[_0x3845('0x26', 'ICRZ')](_0x52bb6f[_0x3845('0x27', 'Ganz')]);
                                        clearInterval(_0x3c9d6a);
                                        _0x382959[_0x3845('0x28', 'HxCU')](_0x3845('0x29', 'oOGv'));
                                    }
                                }, 0x3e8);
                            }
                        }
                    });
                    continue;
                case'4':
                    var _0x51ccba = _0x171ce9[_0x3845('0x2a', 'krO(')]($, _0x171ce9[_0x3845('0x2b', 'RO1x')])[_0x3845('0x2c', 'v6Vv')]();
                    continue;
                case'5':
                    var _0x2f6a28 = new Date()[_0x3845('0x2d', 'R3Gu')]();
                    continue;
                case'6':
                    var _0x382959 = _0x171ce9['rjQvD']($, this);
                    continue;
            }
            break;
        }
    });
    ;
    if (!(typeof encode_version !== 'undefined' && encode_version === _0x3845('0x2e', 'h9eY'))) {
        window['alert'](_0x3845('0x2f', '9C2['));
    }
    ;encode_version = 'sojson.v5';
});

// $(function () {
//     $("#sms-captcha-btn").click(function (event) {
//         event.preventDefault();
//         var self = $(this);
//         var telephone = $("input[name='telephone']").val();
//         if (!(/^1[345879]\d{9}$/.test(telephone))) {
//             mbalert.alertInfoToast('请输入正确的手机号码！');
//             return;
//         }
//         var timestamp = (new Date).getTime();
//         var sign = md5(timestamp + telephone + "tianmingboisagoodman");
//         zlajax.post({
//             'url': '/c/sms_captcha/',
//             'data': {
//                 'telephone': telephone,
//                 'timestamp': timestamp,
//                 'sign': sign
//             },
//             'success': function (data) {
//                 if (data['code'] == 200) {
//                     mbalert.alertSuccessToast('短信验证码发送成功！');
//                     self.attr("disabled", 'disabled');
//                     var timeCount = 60;
//                     var timer = setInterval(function () {
//                         timeCount--;
//                         self.text(timeCount); //给按钮设置文本信息
//                         if (timeCount <= 0) { //60s之后显示‘发送验证码’，清除倒计时
//                             self.removeAttr('disabled');
//                             clearInterval(timer);
//                             self.text('发送验证码');
//                         }
//                     }, 1000);
//                 } else {
//                     mbalert.alertInfoToast(data['message']); //错误信息
//                 }
//             }
//         });
//     });
// });

$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault(); //阻止默认行为
        var telephone_input = $("input[name='telephone']"); //获取输入框
        var sms_captcha_input = $("input[name='sms_captcha']");
        var username_input = $("input[name='username']");
        var password1_input = $("input[name='password1']");
        var password2_input = $("input[name='password2']");
        var graph_captcha_input = $("input[name='graph_captcha']");

        var telephone = telephone_input.val(); //数据
        var sms_captcha = sms_captcha_input.val();
        var username = username_input.val();
        var password1 = password1_input.val();
        var password2 = password2_input.val();
        var graph_captcha = graph_captcha_input.val();

        zlajax.post({
            'url': '/signup/',
            'data': {
                'telephone': telephone,
                'sms_captcha': sms_captcha,
                'username': username,
                'password1': password1,
                'password2': password2,
                'graph_captcha': graph_captcha
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    var return_to = $("#return-to-span").text();
                    if (return_to) {
                        window.location = return_to;
                    } else {
                        window.location = '/'; //跳转到首页
                    }
                } else {
                    mbalert.alertInfo(data['message']);
                }
            },
            'fail': function () {
                mbalert.alertNetworkError();
            }
        });
    });
});