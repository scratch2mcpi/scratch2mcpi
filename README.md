## Scratch2MCPI(Scratch2MinecraftPi)

[日本語の情報](http://scratch2mcpi.github.io/)

With Scratch2MCPI, you can control [Minecraft Pi Edition](http://pi.minecraft.net/) from [Scratch](http://scratch.mit.edu) on Raspberry Pi.

On the latest 2.0, it supports Minecraft Graphics Turtle.

[Demo Movie](https://www.youtube.com/watch?v=w9lkdCEPKWc) on YouTube

## Installation

Install Minecraft Pi Edition if you don't have. You can either install from http://pi.minecraft.net/?p=68 or use the following installation script.(If you install Raspbian OS from the latest NOOBS, Minecraft Pi may be pre-installed. If the Minecraft Pi icon exists on the Desktop, skip this step.)

```
# curl http://scratch2mcpi.github.io/mcpi.sh | sh
```

Install Scratch2MCPI

```
# curl http://scratch2mcpi.github.io/install.sh | sh
```

## Getting Started

1. Start Minecraft, click "Start Game", then "Create New". Wait until the new world is generated.
2. After the world is generated, double click Scratch2MCPI icon to start Scratch and Scratch2MCPI.
3. On Scratch, click Green flag, and run the script. "hello minecraft" should be displayed on Minecraft chat window.

## How to use

You can send the following commands by "broadcast" block of Scratch.

- hello_minecraft: Send "hello minecraft" message to chat section.
- setPos: Move the player to the position specified by Scratch variables: "mcpiX", "mcpiY", "mcpiZ".
- setBlock: Place the block at the position specified by Scratch variables: "mcpiX", "mcpiY", "mcpiZ". The block type and block data can be specified by Scratch variables: "blockTypeId" and "blockData".
- getPos: Get the current position of the player. The position values can be gotten by Scratch sensor values: "PlayerX", "PlayerY", "PlayerZ".
- getHeight: Get the y position of the highest block at the position specified by Scratch variables: "mcpiX" and "mcpiZ". The y postion can be gotten by Scratch sensor value "posY".
- pollBlockHits: Get the block event information of the last block hit by the player. The event info values can be gotten by Scratch sensor values: "blockEventX", "blockEventY", "blockEventZ", "blockEventFace", "blockEventEntityId".
- reset: [WARNING] Reset the world. This will delete clean up the world, so please be aware to use it.

## Reference

- [Minecraft API](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)

## Requirements

- [scratchpy](https://github.com/pilliq/scratchpy)
