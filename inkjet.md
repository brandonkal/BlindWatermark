# Commands

Before running, set REGISTRY in the environment.

## build

```
docker build . -t reg.kite.run/brandonkal/blind-watermark
```

## run//default//embed (image=3-grey.jpg)

> Embed hidden watermark

```sh
docker run -it --rm --mount type=bind,source="$(pwd)",target=/work "$REGISTRY/brandonkal/blind-watermark" \
  -k 4399 2333 32 -em -r "/work/pic/$image" -wm /work/pic/aztec.png -o /work/out.jpg -s
```

## extract

> Extract image data

```sh
docker run -it --rm --mount type=bind,source="$(pwd)",target=/work "$REGISTRY/brandonkal/blind-watermark" \
  -k 4399 2333 32 -ex -r /work/out.jpg -wm /work/pic/aztec.png -ws 64 64 -o /work/out_wm.png -s
```

## small

> Extract image data

```sh
docker run -it --rm --mount type=bind,source="$(pwd)",target=/work "$REGISTRY/brandonkal/blind-watermark" \
  -k 4399 2333 32 -ex -r /work/small.png -wm /work/pic/aztec.png -ws 64 64 -o /work/out_wm_small.png -s
```
