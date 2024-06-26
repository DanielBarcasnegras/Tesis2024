<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;
use Illuminate\Support\Facades\DB;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('images', function (Blueprint $table) {
            $table->id();
            $table->string("image_name");
            #$table->binary("image_file");
            $table->unsignedInteger('ROI_A1_count');
            $table->unsignedInteger('ROI_A2_count');
            $table->unsignedInteger('ROI_A3_count');
            $table->unsignedInteger('ROI_A4_count');
            $table->unsignedInteger('ROI_A5_count');
            $table->unsignedInteger('ROI_A6_count');
            $table->unsignedInteger('ROI_A7_count');
            $table->unsignedInteger('ROI_A8_count');
            $table->unsignedInteger('ROI_B1_count');
            $table->unsignedInteger('ROI_B2_count');
            $table->unsignedInteger('ROI_B3_count');
            $table->unsignedInteger('ROI_B4_count');
            $table->unsignedInteger('ROI_B5_count');
            $table->unsignedInteger('ROI_B6_count');
            $table->unsignedInteger('ROI_B7_count');
            $table->unsignedInteger('ROI_B8_count');
            $table->timestamps();
        });
        DB::statement("ALTER TABLE images ADD image_file LONGBLOB");
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('images');
    }
};
