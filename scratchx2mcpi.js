(function (ext) {

    var BLOCKS = {
      "空気":[0, 0],
      "石":[1, 0],
      "草":[2, 0],
      "土":[3, 0],
      "丸石": [4, 0],
      "木材": [5, 0],
      "苗木": [6, 0],
      "岩盤": [7, 0],
      "水": [8, 0],
      "静止した水": [9, 0],
      "溶岩": [10, 0],
      "ガラス": [20, 0],
      "羊毛(白色)":[35, 0],
      "羊毛(橙色)":[35, 1],
      "羊毛(赤紫色)":[35, 2],
      "羊毛(水色)":[35, 3],
      "羊毛(黄色)": [35, 4],
      "羊毛(黄緑色)": [35, 5],
      "羊毛(桃色)": [35, 6],
      "羊毛(灰色)": [35, 7],
      "羊毛(薄灰色)": [35, 8],
      "羊毛(空色)":[35, 9],
      "羊毛(紫色)":[35, 10],
      "羊毛(青色)":[35, 11],
      "羊毛(茶色)":[35, 12],
      "羊毛(緑色)": [35, 13],
      "羊毛(赤色)": [35, 14],
      "羊毛(黒色)": [35, 15],
      "金ブロック": [41, 0],
      "炎": [51, 0]
    };
    var serverUrl = "http://localhost:8080";
    var blockType = 1;
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

    ext.setblockType = function(blockName) {
      [blockType, blockData] = BLOCKS[blockName];
    };

    ext.setBlockWithBlockName = function(x, y, z, blockName) {
        [_blockType, _blockData] = BLOCKS[blockName];
        $.get(serverUrl + "/set_block/" + x + "/" + y + "/" + z + "/" + _blockType + "/" + _blockData, function() {
            console.log("setBlockWithBlockName succeeded");
        }).fail(function() {
            console.log("setBlockWithBlockName failed!");
        });
    };

    ext.setBlock = function(x, y, z) {
        $.get(serverUrl + "/set_block/" + x + "/" + y + "/" + z + "/" + blockType + "/" + blockData, function() {
            console.log("setBlock succeeded");
        }).fail(function() {
            console.log("setBlock failed!");
        });
    };

    ext.setBlocks = function(x0, y0, z0, x1, y1, z1, blockName) {
      [_blockType, _blockData] = BLOCKS[blockName];
      $.get(serverUrl + "/set_blocks/" + x0 + "/" + y0 + "/" + z0 + "/" + x1 + "/" + y1 + "/" + z1 + "/" + _blockType + "/" + _blockData, function() {
          console.log("setBlocks succeeded");
      }).fail(function() {
          console.log("setBlocks failed!");
      });
    }

    ext._getStatus = function() {
        return { status:2, msg:'Ready' };
    };

    ext._shutdown = function() {};

    var descriptor = {
        blocks: [
            [" ", "リセットする", "reset"],
            [" ", "%s とチャットで送る", "postToChat", "Hello Minecraft"],
            [" ", "ブロックを %m.blockNames にする", "setblockType", "石"],
            [" ", "x:%n y:%n z:%n に移動する", "setPos", 0, 0, 0],
            [" ", "x:%n y:%n z:%n にブロックを置く", "setBlock", 0, 0, 0],
            [" ", "x:%n y:%n z:%n に %m.blockNames のブロックを置く", "setBlockWithBlockName", 0, 0, 0, "石"],
            [" ", "x:%n y:%n z:%n から x:%n y:%n z:%n まで %m.blockNames を置く", "setBlocks", 0, 0, 0, 10, 10, 10, "石"]
        ],
        menus: {
            blockNames: Object.keys(BLOCKS)
        }
    };

    ScratchExtensions.register('ScratchX2MCPI', descriptor, ext);

})({});
