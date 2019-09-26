$(function () {
    $("#save-banner-btn").click(function (event) {
        //点击保存按钮
        event.preventDefault();
        var self = $(this);
        var dialog = $("#banner-dialog");
        var nameInput = $("input[name='name']");
        var imageInput = $("input[name='image_url']");
        var linkInput = $("input[name='link_url']");
        var priorityInput = $("input[name='priority']");


        var name = nameInput.val();
        var image_url = imageInput.val();
        var link_url = linkInput.val();
        var priority = priorityInput.val();
        var submitType = self.attr('data-type'); //获取提交按钮属性,判断是保存还是修改
        var bannerId = self.attr("data-id"); //获取轮播图id

        if (!name || !image_url || !link_url || !priority) {
            mbalert.alertInfoToast('请输入完整的轮播图数据！');
            return;
        }

        var url = ''; //判断是保存还是updata,url不同
        if (submitType == 'update') {
            url = '/cms/update_banner/';
        } else {
            url = '/cms/add_banners/';
        }

        zlajax.post({
            "url": url,
            'data': {
                'name': name,
                'image_url': image_url,
                'link_url': link_url,
                'priority': priority,
                'banner_id': bannerId  //轮播图id
            },
            'success': function (data) {
                dialog.modal("hide");
                if (data['code'] == 200) {
                    // 重新加载这个页面
                    window.location.reload();
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

$(function () {
    $(".edit-banner-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#banner-dialog");
        dialog.modal("show"); //模态框显示

        var tr = self.parent().parent(); //button的父结点的父结点
        var name = tr.attr("data-name"); //获取数据
        var image_url = tr.attr("data-image");
        var link_url = tr.attr("data-link");
        var priority = tr.attr("data-priority");

        var nameInput = dialog.find("input[name='name']"); //获取标签
        var imageInput = dialog.find("input[name='image_url']");
        var linkInput = dialog.find("input[name='link_url']");
        var priorityInput = dialog.find("input[name='priority']");
        var saveBtn = dialog.find("#save-banner-btn");

        nameInput.val(name);//给模态框填充数据
        imageInput.val(image_url);
        linkInput.val(link_url);
        priorityInput.val(priority);
        saveBtn.attr("data-type", 'update'); //更改提交按钮属性为'update'
        saveBtn.attr('data-id', tr.attr('data-id'));
    });
});

$(function () {
    $(".delete-banner-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var banner_id = tr.attr('data-id');
        mbalert.alertConfirm({
            "msg": "您确定要删除这个轮播图吗？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/delete_banner/',
                    'data': {
                        'banner_id': banner_id
                    },
                    'success': function (data) {
                        if (data['code'] == 200) {
                            window.location.reload();
                        } else {
                            mbalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });
    });
});

$(function () {
    zlqiniu.setUp({
        'domain': 'http://7xqenu.com1.z0.glb.clouddn.com/',
        'browse_btn': 'upload-btn',
        'uptoken_url': '/c/uptoken/',
        'success': function (up, file, info) {
            var imageInput = $("input[name='image_url']");
            imageInput.val(file.name);
        }
    });
});