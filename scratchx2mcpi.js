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
      "静止した溶岩": [11, 0],
      "砂": [12, 0],
      "砂利": [13, 0],
      "金鉱石": [14, 0],
      "鉄鉱石": [15, 0],
      "石炭鉱石": [16, 0],
      "原木": [17, 0],
      "葉": [18, 0],
      "ガラス": [20, 0],
      "ラピスラズリ鉱石": [21, 0],
      "ラピスラズリブロック": [22, 0],
      "砂岩": [24, 0],
      "ベッド": [26, 0],
      "クモの巣": [30, 0],
      "草": [31, 0],
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
      "花(タンポポ)": [37, 0],
      "バラ": [38, 0],
      "キノコ(茶)": [39, 0],
      "キノコ(赤)": [40, 0],
      "金ブロック": [41, 0],
      "鉄ブロック": [42, 0],
      "重ねたハーフブロック": [43, 0],
      "ハーフブロック": [44, 0],
      "レンガブロック": [45, 0],
      "TNT": [46, 0],
      "本棚": [47, 0],
      "苔石": [48, 0],
      "黒曜石": [49, 0],
      "松明": [50, 0],
      "炎": [51, 0],
      "樫の木の階段": [53, 0],
      "チェスト": [54, 0],
      "ダイヤモンド鉱石": [56, 0],
      "ダイヤモンドブロック": [57, 0],
      "作業台": [58, 0],
      "耕地": [60, 0],
      "かまど": [61, 0],
      "燃えているかまど": [62, 0],
      "木のドア": [64, 0],
      "はしご": [65, 0],
      "丸石の階段": [67, 0],
      "鉄のドア": [71, 0],
      "レッドストーン鉱石": [73, 0],
      "雪": [78, 0],
      "氷": [79, 0],
      "雪ブロック": [80, 0],
      "サボテン": [81, 0],
      "粘土ブロック": [82, 0],
      "サトウキビ": [83, 0],
      "フェンス": [85, 0],
      "グロウストーン(ブロック)": [89, 0],
      "鍵のかかったチェスト": [95, 0],
      "石レンガ(各種)": [98, 0],
      "板ガラス": [102, 0],
      "スイカ(ブロック)": [103, 0],
      "フェンスゲート": [107, 0],
      "輝く黒曜石": [246, 0],
      "ネザーリアクターコア": [247, 0]
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
