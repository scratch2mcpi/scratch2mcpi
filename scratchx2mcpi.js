(function (ext) {

    var BLOCKS = {
      "空気":[0, 0],
      "石":[1, 0],
      "草":[2, 0],
      "土":[3, 0],
      "丸石": [4, 0],
      "木材": [5, 0],
      "水": [8, 0],
      "金ブロック": [41, 0],
      "炎": [51, 0]
    };
    var serverUrl = "http://localhost:8080";
    var blockTypeId = 1;
    var blockData = 0;

    ext.reset = function() {
        $.get(serverUrl + "/reset", function() {
            console.log("reset succeeded");
        }).fail(function() {
            console.log("reset failed!");
        });
    };

    ext.postToChat = function(str) {
        $.get(serverUrl + "/post_to_chat/" + encodeURIComponent(str), function() {
            console.log("postToChat succeeded");
        }).fail(function() {
            console.log("postToChat failed!");
        });
    };

    ext.setPos = function(x, y, z) {
        $.get(serverUrl + "/set_pos/" + x + "/" + y + "/" + z, function() {
            console.log("setPos succeeded");
        }).fail(function() {
            console.log("setPos failed!");
        });
    };

    ext.setBlockTypeId = function(blockName) {
      [blockTypeId, blockData] = BLOCKS[blockName];
    };

    ext.setBlock = function(x, y, z) {
        $.get(serverUrl + "/set_block/" + x + "/" + y + "/" + z + "/" + blockTypeId + "/" + blockData, function() {
            console.log("setBlock succeeded");
        }).fail(function() {
            console.log("setBlock failed!");
        });
    };

    ext._getStatus = function() {
        return { status:2, msg:'Ready' };
    };

    ext._shutdown = function() {};

    var descriptor = {
        blocks: [
            [" ", "リセットする", "reset"],
            [" ", "%s とチャットで送る", "postToChat", "message"],
            [" ", "ブロックを %m.blockNames にする", "setBlockTypeId", "石"],
            [" ", "x:%n y:%n z:%n に移動する", "setPos", 0, 0, 0],
            [" ", "x:%n y:%n z:%n にブロックを置く", "setBlock", 0, 0, 0],
        ],
        menus: {
            blockNames: Object.keys(BLOCKS)
        }
    };

    ScratchExtensions.register('ScratchX2MCPI', descriptor, ext);

})({});
