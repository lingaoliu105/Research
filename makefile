GEN_NUM = 10

COLOR_MODE = colored

# latex源文件目录
SRC_DIR = output_tex

# pdf目标文件目录
OBJ_DIR = output_pdf

# png图片输出目录
TARGET_DIR = output_png

# json文件输出目录
JSON_DIR = output_json

DATASET_DIR=  my_dataset

SRCS = $(wildcard $(SRC_DIR)/*.tex)

OBJS = $(SRCS:$(SRC_DIR)/%.tex=$(OBJ_DIR)/%.pdf)

TARGETS = $(OBJS:$(OBJ_DIR)/%.pdf=$(TARGET_DIR)/%.png)

IS_CONTAINER := $(shell grep -i docker /proc/self/cgroup > /dev/null && echo "true" || echo "false")


# 默认目标
all: dir tex pdf png labels

dir:
	mkdir -p $(OBJ_DIR)
	mkdir -p $(SRC_DIR)
	mkdir -p $(TARGET_DIR)
	mkdir -p $(JSON_DIR)

tex: dir gen_rand_tikz.py
	python gen_rand_tikz.py $(GEN_NUM) $(COLOR_MODE)

$(OBJ_DIR)/%.pdf : $(SRC_DIR)/%.tex

	@if [ "$(IS_CONTAINER)" = "true" ]; then pdflatex -interaction=batchmode -output-directory=$(OBJ_DIR) $< ; fi
	

pdf: $(OBJS)
	@if [ "$(IS_CONTAINER)" = "false" ]; then \
		echo "Running in WSL environment."; \
		docker-compose up; \
	else \
		echo "Not running in WSL environment."; \
	fi


$(TARGET_DIR)/%.png : $(OBJ_DIR)/%.pdf
	python convert_image.py $<

png: $(TARGETS)
	cp $(TARGET_DIR)/* $(DATASET_DIR)/data

labels:
	python combine_json.py $(GEN_NUM)

show:
	python dataset_visualization.py

# 清理生成的文件
clean:
	rm -f $(SRC_DIR)/* $(OBJ_DIR)/* $(TARGET_DIR)/* $(JSON_DIR)/*

# PHONY 目标表示这些目标不是实际文件
.PHONY: all clean