# Commands

Before running, set DOCKER_HOST in the environment.

## build

```
docker build . -t reg.kite.run/brandonkal/blind-watermark
```

## run//default

> Embed hidden watermark

```sh
docker run -it --rm --mount type=bind,source="$(pwd)",target=/work "$DOCKER_HOST/brandonkal/blind-watermark" \
  -k 4399 2333 32 -em -r /work/pic/3-grey.jpg -wm /work/pic/qr.png -o /work/out.jpg -s
```

## extract

> Extract image data

```sh
docker run -it --rm --mount type=bind,source="$(pwd)",target=/work "$DOCKER_HOST/brandonkal/blind-watermark" \
  -k 4399 2333 32 -ex -r /work/out.jpg -wm /work/pic/qr.png -ws 100 100 -o /work/out_wm.png -s
```

## small

> Extract image data

```sh
docker run -it --rm --mount type=bind,source="$(pwd)",target=/work "$DOCKER_HOST/brandonkal/blind-watermark" \
  -k 4399 2333 32 -ex -r /work/small.png -wm /work/pic/qr.png -ws 100 100 -o /work/out_wm_small.png -s
```
